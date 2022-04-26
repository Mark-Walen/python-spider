import requests
import xlwt
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
    soup.prettify()
    items = soup.select('.item')
    for item in items:
        text = str(item.select('.bd p')[0].get_text().replace(u'\xa0', u'').strip())
        dir_end = text.find("主")
        ac_end = text.find("\n")
        new_text = text.replace(u'\n', u'').split('/')
        time_start = new_text[-3].find("...") + 20
        yield {
            'index': item.select('em')[0].get_text(),
            'image': item.select('img')[0].attrs['src'],
            'title': item.select('.title')[0].get_text(),
            'director': text[3:dir_end].strip(),
            'actor': text[dir_end + 4:ac_end],
            'time': new_text[-3][time_start:].strip(),
            'nation': new_text[-2],
            'plot': new_text[-1],
            'star': item.select('.rating_num')[0].get_text()
        }


def write_to_excel(filename, content):
    try:
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("豆瓣top250")
        heads = ['index', 'image', 'title', 'director', 'actor', 'time', 'nation', 'plot', 'star']
        for i in range(len(heads)):
            ws.write(0, i, heads[i])
        row = 0
        for item in content:
            row += 1
            ws.write(row, 0, item['index'])
            ws.write(row, 1, item['image'])
            ws.write(row, 2, item['title'])
            ws.write(row, 3, item['actor'])
            ws.write(row, 5, item['time'])
            ws.write(row, 8, item['star'])
        wb.save(filename)
        print('写入成功')
    except Exception:
        print("写入失败")


def main(start=0):
    url = 'https://movie.douban.com/top250?start=' + str(start)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
    return parse_one_page(html)


if __name__ == '__main__':
    contents = []
    for i in range(10):
        contents.extend(main(i*25))
    # write_to_excel('douban.xls', contents)