# 解析链接
# 1.urlparse()
#   参数
#   * urlstring
#   * scheme
#   * allow_fragments
# 2.urlunparse()
# 接受的参数是一个可迭代对象,但是它的长度必须是6,否则会抛出参数数量不足或过多问题.
# 3.urlsplit()
# 和urlparse()方法相似,只不过它不再单独解析params这一部分,只返回5个结果,params会合并到path.
# 4.urlunsplit()
# 和urlunparse()方法相似,接受的参数是一个可迭代对象,但是它的长度必须是5.
# 5.urljoin()
# 我们可以提供一个base_url作为第一个参数,将新的链接作为第二个参数,
# 该方法会分析base_url的scheme、netloc和path
# base_url提供了三项内容base_url的scheme、netloc和path.如果这三项在新的链接里不存在，
# 就予以补充.如果新的链接存在,就使用新的链接的部分。而base_url中的params、query和fragment是不起作用的
# 6.urlencode()
# 在构造GET请求参数的时候非常有用
# 7.parse_qs()

from urllib.parse import urlparse, urljoin, urlencode

result = urlparse('http://baidu.com/index.html;user?id=5#comment')
print(type(result), result)

print(urljoin('http://baidu.com', 'FAQ.html'))
print(urljoin('http://baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))

params = {
    'name': 'germey',
    'age': 22
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)