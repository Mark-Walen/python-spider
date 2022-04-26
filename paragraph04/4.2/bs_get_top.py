import json

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('dd')
    for item in items:
        yield {
            'index': item.i.string,
            'image': item.find(class_='board-img')['data-src'],
            'title': item.find(class_='name').string,
            'actor': item.find(class_='star').text.strip(),
            'time': item.find(class_='releasetime').text.strip(),
            'star': item.find(class_='integer').string.strip()+item.find(class_='fraction').string.strip()
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content['src'])))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)