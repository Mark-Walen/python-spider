from bs4 import BeautifulSoup


soup = BeautifulSoup(open('result.html', encoding='utf-8'), 'lxml')
items = soup.find_all(attrs={'class': 'reader-word-layer'})
for item in items:
    print(item.string)