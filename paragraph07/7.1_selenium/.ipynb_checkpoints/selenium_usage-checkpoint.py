from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 初始化浏览器对象
browser = webdriver.Chrome()

"""
# 1. 基本使用 selenium
try:
    browser.get('https://www.baidu.com')
    inp = browser.find_element_by_id('kw')
    # 搜索关键字
    inp.send_keys('Python')
    # 执行确认键，进行搜索
    inp.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)

finally:
    browser.close()
"""

"""
# 2. 访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()
"""

"""
# 3. 查找节点
#   1) 单个节点
#       所有方法：
#           find_element_by_id
#           find_element_by_name
#           find_element_by_xpath
#           find_element_by_link_text
#           find_element_by_partial_link_text
#           find_element_by_tag_name
#           find_element_by_class_name
#           find_element_by_css_selector
#       通用方法
#           find_element()
#           @param By 查找方式
#           @param val 值

browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_fourth = browser.find_element(By.ID, 'q')
print('{0}\n{1}\n{2}\n{3}\n'.format(input_first, input_second, input_third, input_fourth))
browser.close()
"""
