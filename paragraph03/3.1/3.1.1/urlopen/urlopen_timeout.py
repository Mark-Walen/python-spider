import urllib.request

# timeout参数
response = urllib.request.urlopen('http://httpbin.org.get', timeout=2)
print(response.read())
