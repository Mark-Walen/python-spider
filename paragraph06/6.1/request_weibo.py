from urllib.parse import urlencode
import requests
from pymongo import MongoClient
import time

base_url = 'https://weibo.com/ajax/statuses/mymblog?'

headers = {
    'Host': 'weibo.com',
    'referer': 'https://weibo.com/u/7498971049',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/93.0.4577.82 Safari/537.36 ',
    'X-Requested-With': 'XMLHttpRequest',
    'x-xsrf-token': 'h3ePn_lBR9VcMh_DKtfMThWG',
    'accept': 'application/json, text/plain, */*',
    'cookie': 'SINAGLOBAL=1848248060811.9167.1610854889009; UOR=www.google.com,weibo.com,www.google.com.hk; '
              'ULV=1631884613820:2:1:1:5931861270585.2705.1631884613807:1610854889031; '
              'SUB=_2A25MQOUpDeRhGeNJ6lQT8SvOwj6IHXVvyothrDV8PUJbkNANLRPHkW1NS-S87VyY2w_PB3XZS7UIvL-wXdkAe1sr; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF.xMjkrRAb8BBX6Ime.jli5NHD95QfS02ceo2feo.EWs4Dqcj_i--fi-8siKnEi'
              '--fiKnXiK.Ei--NiKLWiKnXi--ci-zNi-zpi--ci-zRiKyW; '
              'WBPSESS=GHWsvE1YqmFMO9BF7my-5u9bf69hxS'
              '-6JwgQdjkn7N9EqygQxcukjmr0jC1FCsairIrV7sXDmYUPJWWsGOmY8TrxFEcf6HaxB4rS7-41LB2ZSoIjsp0xIjpI__Fqe7E8; '
              'XSRF-TOKEN=h3ePn_lBR9VcMh_DKtfMThWG '

}

client = MongoClient('mongodb://localhost:27017/')
db = client['weibo']
collection = db['weibo']
prev_since_id = ''


def get_page(page, since_id=''):
    params = {
        'uid': '7498971049',
        'page': page,
        'feature': '0',
    }
    # 第一次请求页面时 since_id 为空，所以
    if since_id != '':
        params['since_id'] = since_id
    url = base_url + urlencode(params)
    s = requests.session()
    s.proxies = {'http': '182.84.144.180:3256'}
    try:
        response = s.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


# pyquery将正文的 HTML 标签去掉
def parse_page(resp_json):
    if resp_json:
        items = resp_json.get('data').get('list')
        for item in items:
            weibo = {
                'id': item.get('id'),
                'created_at': item.get('created_at'),
                'attitudes_count': item.get('attitudes_count'),
                'comments_count': item.get('comments_count'),
                'reposts_count': item.get('reposts_count'),
                'source': item.get('source'),
                'text': item.get('text'),
                'text_raw': item.get('text_raw')
            }
            print(weibo)
            yield weibo


def save_to_mongo(result):
    if collection.insert_many(result):
        print('Saved to mongo')


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page, prev_since_id)
        time.sleep(2)
        if json:
            prev_since_id = json.get('data').get('since_id')
            res = parse_page(json)
            save_to_mongo(res)
        else:
            print('请求失败')
