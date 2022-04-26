# 1.文件上传
# 文件删除部分会单独有一个files字段来标识。
# 2.Cookies
# 3.会话维持
#   Session对象
# 4.SSL证书验证

import requests

files = {'file': open('../3.2.1/favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)