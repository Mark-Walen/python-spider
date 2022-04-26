import requests
import os
import re
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool


base_url = 'https://so.toutiao.com/search?'


# 由于今日头条的接口已经换了，所以不再进行练习，主要目的学会下载图片
def get_page(page_num, keyword):
    headers = {
        'host': 'so.toutiao.com',
        'cookie': '_S_DPR=1; _S_IPAD=0; MONITOR_WEB_ID=7009570034055169566; '
                  'ttwid=1%7CHV7908xPl980w6hiyHjLZEr01XoGF5PByOK76AaFNCM%7C1632063560'
                  '%7C10324db0889fd1667c288a4b2e88854c642242de9b658d7d79280ede3ce8bb09; _S_WIN_WH=1144_976 ',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36 ',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9 '

    },
    params = {
        'dvpf': 'pc',
        'source': 'input',
        'keyword': keyword,
        'page_num': page_num,
        'pd': 'synthesis'
    }
    url = base_url + urlencode(params)
    headers.referer = url
    s = requests.session()
    s.proxies = {'http': '182.84.144.180:3256'}
    try:
        response = s.get(url, headers=headers)
        if response.status_code == 200:
            return response
    except requests.ConnectionError as e:
        print('Error', e.args)
