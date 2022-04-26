from bs4 import BeautifulSoup
import re


file = open('ul_from_tb.html', encoding='UTF-8')
try:
    content = file.read()
    pattern = re.compile('role="(.*)^"')
    result = re.findall(pattern, content)
    print(result)
finally:
    file.close()
