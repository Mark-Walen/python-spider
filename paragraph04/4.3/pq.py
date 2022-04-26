# 1.初始化
#   *字符串初始化
#   *URL初始化
# 2.基本CSS选择器
# 3.查找节点
#   *子节点
#   find()方法

from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
print(doc('li'))