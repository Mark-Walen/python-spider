import re
import time

import requests
from requests.exceptions import RequestException


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
    pattern = re.compile('<li>.*?class="">(.*?)</em>.*?src="(.*?)".*?class="title">(.*?)</span>.*?导演:(.*?)主演:('
                         '.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n.*?property="v:average">(.*?)</span>',
                         re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'director': item[3].strip()[:-18],
            'actor': item[4],
            'time': item[5].strip()[-4:],
            'nation': item[6],
            'plot': item[7],
            'star': item[8]
        }


def main(start=1):
    url = 'https://movie.douban.com/top250?start=' + str(start)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)


if __name__ == '__main__':
    for i in range(10):
        main(start=25*i)
    time.sleep(1)
