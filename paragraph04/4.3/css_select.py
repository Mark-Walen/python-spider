from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
print(doc('#container .list li'))
print(type(doc('#container .list li')))
