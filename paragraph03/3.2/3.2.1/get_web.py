import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61 '
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
patten = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(patten, r.text)
print(titles)