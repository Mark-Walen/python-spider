import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("https://httpbin.org/post", data=data)
print(r.text)

r2 = requests.get('http://www.jianshu.com')
print(type(r2.status_code), r2.status_code)
print(type(r2.headers), r2.headers)
print(type(r2.cookies), r.cookies)
print(type(r2.url), r2.url)
print(type(r2.history), r2.history)
