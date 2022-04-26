import requests

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
headers = {
    'cookie': 'zap=17bd328c-c829-41e0-a0a0-3864afc0cd71; d_c0="AMCbIx_QdxGPTq7kGneMAbkPxRY6uRSoF_c=|1592878288"; '
              '_ga=GA1.2.467942225.1592878290; _xsrf=DLdD9YEnFpQymJadJ5Z6FlOVpxaa7txQ; '
              'z_c0=Mi4xcEprQUR3QUFBQUFBd0pzakg5QjNFUmNBQUFCaEFsVk5QRzdsWHdCV3Z2dzJqYWNPS29CQ21ESGU3STBiTjZhWml3'
              '|1593319484|c017ca4af044ff44b1881cb9c19c9f20142bdbe1; '
              'q_c1=86ac63712eb045d58561315d65f724fd|1596621278000|1593319558000; _gid=GA1.2.645734721.1597844558; '
              'tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1596784048,1597663758,1597844558,1597888638; '
              'SESSIONID=k5qi24doKhYzuhnoAWfPNDaQ21Id5XokkbkGODNg5lI; '
              'JOID=Vl4dA013rObpgeHmFnN8fMqiKmsLHpefhrHXjHE-xrGb8ouKdwJy1bKB7eAYMHpoy4bGhOxJHiyBk3DR7k6fhHk=; '
              'osd=VF4XBEN1rOzuj-PmHHRyfsqoLWUJHp2YiLPXhnYwxLGR9YWIdwh127CB5-cWMnpizIjEhOZOEC6BmXff7E6Vg3c=; '
              'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1597888648; '
              'KLBRSID=3d7feb8a094c905a519e532f6843365f|1597888977|1597888630',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
