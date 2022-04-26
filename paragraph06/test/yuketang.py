from bs4 import BeautifulSoup
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55',
    'Cookie': 'viewedPg=117e5213f18583d04964594e%3D9%7C0%26f8f181c5bb4cf7ec4afed0c6%3D3%7C0'
              '%2616888bea4afe04a1b071dece%3D1%7C0%26ec42c4c93a3567ec102de2bd960590c69ec3d8cc%3D9%7C0'
              '%26f69ff93f3186bceb18e8bb41%3D2%7C0; wkview_gotodaily_tip=1; murmur=undefined--Win32; '
              'BIDUPSID=BC12E0F634FA96D5BB7CD1CD9266EBDD; BAIDUID=C37A83E93C0870542D4A0392A0E2A20A:FG=1; '
              'PSTM=1605702969; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; _click_param_reader_query_ab=-1; '
              '_click_param_pc_rec_doc_2017_testid=4; layer_show_times_total_2_b5c8647dd042e9b58f881682bc0f41a3=13; '
              'BDUSS=kZBYWloSnVUcWhQaXZPSlBLbUJQNVNMVmF1SkZTcmFMUWV0NWNaOHc0UHBkLTFmRVFBQUFBJCQAAAAAAAAAAAEAAADitqSfsKLI~TkwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOnqxV~p6sVfd; BDUSS_BFESS=kZBYWloSnVUcWhQaXZPSlBLbUJQNVNMVmF1SkZTcmFMUWV0NWNaOHc0UHBkLTFmRVFBQUFBJCQAAAAAAAAAAAEAAADitqSfsKLI~TkwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOnqxV~p6sVfd; __cfduid=db35fc49880fb15a0c2c232a85e8514a01606807733; Hm_lvt_de54c5cc453c7904719695d12c1a5daa=1606552969,1607090554,1607090564; BAIDUID_BFESS=C37A83E93C0870542D4A0392A0E2A20A:FG=1; bcat=4b59447f961487bd95719035ee5753105834055152b5e5c7da9359f562df466ecac564c6f560a6a0b5baf9520b2160dc14f748761bac4ecc652678b791979106e0f3564c521fc7904bc5b3c99380fe7fe3b5598d9eba2e40a34668c75fe1d271b1e91586e4a79e4e7cc997fd5dce6f1c35bf31333445443a413e5eeec80ad4b4; delPer=0; PSINO=6; H_PS_PSSID=1451_33103_33117_33059_33099_33101_32846_33199_33238_33147_22159; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1607003465,1607154869,1607321291,1607322514; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1607322514; LoseUserAllPage=%7B%22status%22%3A0%2C%22expire_time%22%3A0%2C%22create_time%22%3A1607322532%2C%22type%22%3A0%2C%22cookie_time%22%3A1607581732%7D; Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1605574067,1607322533; Hm_lpvt_f06186a102b11eb5f7bcfeeab8d86b34=1607322533; close_cashier_time_3_b5c8647dd042e9b58f881682bc0f41a3=1; ___wk_scode_token=eUXmSpZeC1eLktT1nyyp3RzIkeglFwE2XFyqQOrb7ZI%3D',
    'referer': 'https://wenku.baidu.com/view/20a6e22d4793daef5ef7ba0d4a7302768e996fbb.html'
}

url = 'https://wkbjcloudbos.bdimg.com/v1/docconvert4610/wk/482d5066c9f85b61d539175d990e967e/0.png?responseContentType=image%2Fpng&amp;responseCacheControl=max-age%3D3888000&amp;responseExpires=Thu%2C%2021%20Jan%202021%2017%3A09%3A18%20%2B0800&amp;authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-12-07T09%3A09%3A18Z%2F3600%2Fhost%2F3424ad87c2d2eee0227d06b87c32ba83ee07ec86969514b9f8605c6a0d5dca8f&amp;x-bce-range=314-660&amp;token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYwNzMzNTc1OCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.9xQzR80MEsF6Za2d4lTM1l2VaMYLbBAKAsdR2XTesUM%3D.1607335758'
resp = requests.get(url, headers=headers)
try_time = 0
while try_time < 3:
    if resp.status_code == 200:
        with open('result.html', 'w',encoding='utf-8') as f:
            f.write(resp.text)
        try_time = 3
    else:
        try_time += 1