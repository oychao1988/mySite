import os

import requests
from faker import Factory
import time
from selenium import webdriver

from myScrapy.settings import PROXY_POOL_SERVER

fake = Factory.create('zh_CN')
user_agent = fake.user_agent()
proxy = 'http://' + requests.get(PROXY_POOL_SERVER).text

# seleniuim 登录、验证、爬取
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--user-agent=%s' % user_agent)
chromeOptions.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')

# 获取查询结果页面
def index(keyword):
    # 打开首页
    index_url = 'http://www.gsxt.gov.cn/'
    driver.get(index_url)

    # 在输入框输入关键字
    while True:
        try:
            time.sleep(10)
            driver.find_element_by_id('keyword').send_keys(keyword)
            time.sleep(5)
            driver.find_element_by_id('btn_query').click()
            time.sleep(20)
            page_source = driver.page_source
        except Exception as e:
            print(e)
            driver.refresh()
            continue
        # 如果返回内容为有效信息，则继续
        if page_source:
            break
    with open('search_list.txt', 'wb') as f:
        f.write(page_source)
    print('search_list已保存')

# 定位点击进入详情页位置
def detail_elements():
    elements = driver.find_element_by_id('')
    return elements

def detail(element):
    while True:
        try:
            element.click()
            time.sleep(10)
            # 滚动到页面最底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(10)
        except Exception as e:
            print(e)
            time.sleep(10)
            continue
        page_source = driver.page_source
        # 如果返回内容为有效信息，则继续
        if page_source:
            driver.back()
            break
    with open('detail.txt', 'wb') as f:
        f.write(page_source)
    print('detail已保存')

if __name__ == '__main__':
    keyword = '传智播客'
    index(keyword)
    # 获取当前页面的所有结果
    elements = detail_elements()
    for element in elements:
        detail(element)
    # 进入下一页