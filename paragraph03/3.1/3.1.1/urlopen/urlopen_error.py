import socket
import urllib.request
import urllib.error

# timeout参数
try:
    response = urllib.request.urlopen('http://httpbin.org.get', timeout=2)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
