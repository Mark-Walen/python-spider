# 提取信息
#   1.获取名称
#       调用name属性
#   2.获取属性
#       调用attrs获取所有属性
#   3.关联选择
#       *子节点和子孙节点
#       contents属性得到的结果是直接子节点的列表
#       子孙节点：调用children属性，返回结果是生成器类型
#       获得所有子孙节点：调用descendants属性
#       *父节点和祖先节点
#        父节点：调用parent属性
#       *兄弟节点
#   4.提取信息
# 方法选择器
# CSS选择器
# 调用select()方法
#   find_all(name, attrs, recursive, text, **kwargs)
import re

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'lxml')
# print(soup.prettify())
# print(soup.title.string)
# # 选择元素
# print(soup.head)
# print(soup.p)
# print(soup.title.name)
#
# print(soup.p.attrs)
# # 获取name属性，就相当于从字典获取某个键值。
# print(soup.p.attrs['name'])
#
# print(soup.p.contents)
#
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
#
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
#
# print(soup.a.parent)
# 获取所有祖先节点
# print(list(enumerate(soup.a.parents)))
# 兄弟节点
# print('Next Sibling', soup.a.next_sibling)
# print('Next Sibling', soup.a.previous_sibling)
# print('Next Sibling', list(soup.a.next_sibling))
# print('Next Sibling', list(soup.a.previous_sibling))
soup = BeautifulSoup(open('../4.1/test.html'), 'lxml')
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)
print(soup.find_all(attrs={'name': 'item'}))
print(soup.find_all(text=re.compile('item')))
