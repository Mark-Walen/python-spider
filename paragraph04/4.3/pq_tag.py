# 节点操作

from pyquery import PyQuery as pq

doc = pq(filename='../4.1/test.html')
# addClass removeClass
li = doc('.item-inactive')
print(li)
# li.addClass('active')
# print(li)
# li.removeClass('active')
# print(li)
# attr、text和html
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)
# remove()

li.text('third item')
print(li)
