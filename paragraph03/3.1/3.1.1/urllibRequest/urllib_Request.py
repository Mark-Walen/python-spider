import urllib.request

request = urllib.request.Request('http://python.org')
# request = urllib.request.Request('https://www.renrendoc.com/paper/93940623.html')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))