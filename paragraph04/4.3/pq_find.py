from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
# # 查找所有符合条件的子节点，调用children()方法传入CSS选择器
# lis = items.children('.item-0')
# print(lis)
# container = items.parent()
# print(type(container))
# print(container)
# 兄弟节点
li = doc('.list .item-inactive')
print(li.siblings())
