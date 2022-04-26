# 请求的链接自动被构造成了： http:／／htφbin.org/get?age=22&name=germey
# 4.Post请求
# 5.响应

import requests
import os

data = {
    "name": 'germey',
    "age": 22
}

# r = requests.get('https://httpbin.org/get')
r = requests.get('https://httpbin.org/get', params=data)
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)


