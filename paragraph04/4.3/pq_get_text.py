from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
a = doc('.item-0 a')
print(a)
print(a.text())
