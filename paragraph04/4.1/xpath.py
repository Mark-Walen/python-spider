# 调用tostring()方法即可输出修正后的HTML代码，但结果是bytes类型。

from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">first item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
# 匹配所有节点
# result = html.xpath('//*')
# 指定节点名称
# result = html.xpath('//li')
# 子节点
# result = html.xpath('//li/a')
# 父节点
# 也可以通过parent::来获取父节点
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# 属性匹配
# result = html.xpath('//li[@class="item-0"]')
# 文本获取
# result = html.xpath('//li[@class="item-0"]/text()')
# result = html.xpath('//li[@class="item-0"]/a/text()')
# result = html.xpath('//li[@class="item-0"]//text()')
# 属性获取
# result = html.xpath('//li/a/@href')
# 属性多值匹配
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# 多属性匹配
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# 按序选择
# result = html.xpath('//li[1]/a/text()')
# result = html.xpath('//li[last()]/a/text()')
# result = html.xpath('//li[position()<3]/a/text()')
result = html.xpath('//li[last()-2]/a/text()')
print(result)
