# 对于单个节点来说，可以直接打印输出，也可以转成字符串
# 对于多个节点的结果，需要遍历来获取。

from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
# li = doc('.item-inactive')
# print(li)
# print(str(li))

lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
