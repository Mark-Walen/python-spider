# 3.1 使用urllib
#   urllib库是python内置的HTTP请求库
#   四个模块：
#       request：是最基本的HTTP请求模块，可以用来模拟发送请求
#       error：异常处理模块，如果出现请求错误我们可以捕获这些异常，然后进行重试或其他操作
#       以保证程序不会意外终止。
#       parse：一个工具模块，提供许多URL处理方法，比如拆分、解析、合并等。
#       主要用来识别网站的robots.txt文件，然后判断哪些网站可以爬取，哪些网站不可以爬取
#   3.1.1 发送请求
#       1.urlopen()
#       参数列表：
#       * data：如果传递了这个参数，则他的请求方式不再是GET方式，而是POST方式
#       * timeout
#       2.Request()
#       参数列表
#       * url
#       * data: 必须传bytes(字节流)类型。如果是字典可以先用urllib。parse模块里的urlencode()编码
#       * headers：是一个字典，它就是请求头，可以通过headers参数直接构造，也可以通过调用
#       请求实例的add_header()方法来添加
#       * origin_req_host
#       * unverifiable：默认是False
#       * method：用来指示请求使用的方法

import urllib.request
import urllib.parse

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
print(type(response))

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
