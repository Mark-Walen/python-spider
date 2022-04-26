import requests

# 代理无效
# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
proxies = {
    'http': 'socks5://user:password@host:port',
    'http': 'socks5://user:password@host:port'
}

requests.get("https://www.taobao.com", proxies=proxies)
