import urllib.request
import urllib.parse


# data参数
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding= 'utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())