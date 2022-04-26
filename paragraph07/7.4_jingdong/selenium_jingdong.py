import random
import time
from urllib.parse import quote

import pymongo
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式
browser = webdriver.Chrome(options=chrome_option)
wait = WebDriverWait(browser, 20)
KEYWORD = '薄膜键盘'

MONGO_URL = 'localhost'
MONGO_DB = 'jingdong'
MONGO_COLLECTION = 'products'
MAX_PAGE = 20
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

retry = 0


def mock_scroll():
    scroll_height = 466
    # 模拟手动滚动
    for i in range(1, 22):
        browser.execute_script('window.scrollTo(' + str((i - 1) * scroll_height) + ',' + str(i * scroll_height) + ')')
        time.sleep(random.uniform(0.5, 2))


def index_page(page):
    global retry
    """
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        # url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        url = 'https://search.jd.com/Search?keyword=' + quote(KEYWORD)
        browser.get(url)
        mock_scroll()
        if page > 1:
            search_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.page .p-skip .input-txt'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.page .p-skip .btn'))
            )
            search_input.clear()
            search_input.send_keys(page)
            browser.execute_script("arguments[0].click();", submit)
            time.sleep(1)
        html = browser.page_source
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.page .p-num .curr'), str(page))
        )
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList .gl-warp .gl-item .gl-i-wrap')))
        get_products(html)
        # 爬取完后回到顶部
        back_to_top = browser.find_element_by_css_selector('.jdm-tbar-tab-top .tab-ico')
        browser.execute_script("arguments[0].click();", back_to_top)
    except TimeoutException:
        print("已超时")
        if retry < 5:
            retry += 1
            index_page(page)


def get_products(html):
    """
    提取商品数据
    """
    doc = pq(html)
    items = doc('#J_goodsList .gl-warp .gl-item').items()
    for item in items:
        img = item.find('.p-img > a > img').attr('src')
        key = 'https:' + item.find('.p-name a').attr('href')
        if img is not None:
            img = 'https:' + img
        else:
            img = item.find('.p-img > a > img').attr('data-lazy-img')
            if img is not None:
                img = 'https:' + img
            else:
                img = ''
        product = {
            # J_goodsList > ul > li:nth-child(42) > div > div.p-img > a > img
            'sku-href': key,
            'image': img,
            'price': item.find('.p-price').text(),
            'commit': item.find('.p-commit').text(),
            'title': item.find('.p-name a em').text(),
            'shop': item.find('.p-shop .J_im_icon > a.curr-shop').text(),
            'location': item.find('.p-stock').attr('data-province'),
        }
        print(product)
        save_to_mongo(product, key)


def save_to_mongo(result, key):
    """
    保存至 MongoDB
    :param key: 查询是否存在的键值
    :param result: 结果
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert_one(result):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE+1):
        index_page(i)


if __name__ == '__main__':
    main()
    # index_page(1)
