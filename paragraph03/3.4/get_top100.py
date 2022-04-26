import json
import time
from requests.exceptions import RequestException
import requests
import re
import xlwt


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
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def write_to_excel(filename, content):
    try:
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('猫眼电影top100')
        heads = ['index', 'image', 'title', 'actor', 'time', 'score']
        for i in range(len(heads)):
            sheet.write(0, i, heads[i])
        for i in range(10):
            row = i*10
            for item in content:
                row += 1
                sheet.write(row, 0, item['index'])
                sheet.write(row, 1, item['image'])
                sheet.write(row, 2, item['title'])
                sheet.write(row, 3, item['actor'])
                sheet.write(row, 4, item['time'])
                sheet.write(row, 5, item['score'])
        work_book.save(filename)
        print('写入成功')
    except Exception:
        print('写入失败')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # for item in parse_one_page(html):
    #     print(item)
    #     write_to_file(item)
    # print(html)
    content = parse_one_page(html)
    write_to_excel('top100.xls', content)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
