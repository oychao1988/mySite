from lxml import etree

import requests
import time
from faker import Factory
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from myScrapy.settings import PROXY_POOL_SERVER
from myScrapy.utils.utils import cookie_transfer

searchword = '阿里巴巴'
index_url = 'http://www.gsxt.gov.cn/'
# token_url = 'http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html?token=4427009074'

search_url = 'http://www.gsxt.gov.cn/corp-query-search-test.html?searchword=%s' % searchword

detail_url = 'http://www.gsxt.gov.cn/corp-query-search-1.html'

fake = Factory.create('zh_CN')
# headers_str = """Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding:gzip, deflate
# Accept-Language:zh-CN,zh;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# Content-Length:245
# Content-Type:application/x-www-form-urlencoded
# Cookie:__jsluid=5316a8bd816fb2fac79dd58b328dcb9d; __jsl_clearance=1540047737.709|0|VATBrfVv81SNlcS%2BvhM6%2B3%2BPUbw%3D; SECTOKEN=7077903105422790290; UM_distinctid=166921abd732d5-0bf6b3603849cd-3e70055f-100200-166921abd742e; CNZZDATA1261033118=1924476378-1540046316-null%7C1540046316; tlb_cookie=S172.16.12.71; JSESSIONID=E66DB29E20A0354CE4CC66CF7A0924D4-n2:-1
# Host:www.gsxt.gov.cn
# Origin:http://www.gsxt.gov.cn
# Referer:http://www.gsxt.gov.cn/index.html
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"""

# cookies_str = "__jsluid=5316a8bd816fb2fac79dd58b328dcb9d; UM_distinctid=166921abd732d5-0bf6b3603849cd-3e70055f-100200-166921abd742e; CNZZDATA1261033118=1924476378-1540046316-null%7C1540046316; __jsl_clearance=1540081394.901|0|9O2oFniFrMjnBC4925bRmdpxudo%3D; SECTOKEN=7077480743472729311; tlb_cookie=S172.16.12.42; JSESSIONID=DE6A78A52635592505674E28D581C6E2-n1:0"
#
# cookies_dict = cookie_transfer(cookies_str)


def plan_request(url):
    count = 0
    while True:
        count += 1
        print('第%d次连接'%count)
        try:
            headers = {  # 'Origin': 'http://www.gsxt.gov.cn',
                # 'Referer': 'http://www.gsxt.gov.cn/index',
                'Referer': url,
                'Upgrade-Insecure-Requests': '1',
                # 'Cookie': cookie_dict,
                # 'User-Agent': fake.user_agent(),
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            }
            proxy = 'http://' + requests.get(PROXY_POOL_SERVER).text
            session = requests.Session()
            # session.headers.update(headers)
            session.proxies = {'http': proxy}
            # response = session.get(index_url)
            # response = requests.get(url, headers=headers, cookies=cookie_dict, proxies={'http': proxy})
            response = requests.get(url, headers=headers, proxies={'http': proxy})
            # response = session.get(url, headers=headers)
            # response = requests.get(url, headers=headers, cookies=cookie_dict)

            # url = response.request.url
            # header = response.headers
            # _cookie = response.request._cookies
            print('status_code:', response.status_code)
        except Exception as e:

            print(e)
            continue
        if response.status_code not in [500, 521, 503]:
            break
        time.sleep(5)
    print('*'*50)
    print(response.content.decode())
    # result = session.get(token_url)
    # print(result)
    # result = session.get(search_url)
    # print(result)
    # html = session.get(detail_url).content
    # print(html.decode())

import os
from selenium import webdriver

def start_browser(browser, url):
    # browser = webdriver.Chrome(os.getcwd() + '/chromedriver')
    # print('before request cookies:', browser.get_cookies())
    # browser.delete_all_cookies()
    #
    # for k, v in cookies.items():
    #     print({'name': k, 'value': v})
    #     browser.add_cookie({k + ':' + v})
    time.sleep(5)
    browser.get(url)
    time.sleep(10)
    page_source = browser.page_source
    browser.quit()
    print('*+*+'*10)
    print(page_source)

def plan_selenium():
    keyword = '传智播客'
    browser = webdriver.Chrome(os.getcwd() + '/chromedriver')

    # 使用代理，但无法使用
    # proxy = 'http://' + requests.get(PROXY_POOL_SERVER).text
    # print(proxy)
    # add_proxy = "--proxy-server=" + proxy
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument(add_proxy)
    # browser = webdriver.Chrome(os.getcwd() + '/chromedriver', chrome_options=chromeOptions)

    # 避免速度过快，获取不到网页
    browser.get(index_url)
    time.sleep(10)

    # browser.get("http://httpbin.org/ip")
    # page_source = browser.page_source
    # print(page_source)
    browser.find_element_by_id('keyword').send_keys(keyword)
    time.sleep(10)
    browser.find_element_by_id('btn_query').click()
    time.sleep(20)
    # page_source = browser.page_source
    # print('detail_page:', page_source)

    # html = etree.HTML(page_source)
    # hrefs = html.xpath("//div[@class='main-layout fw f14']/div[2]/a/@href")
    # print(hrefs)
    # detail_urls = [index_url + url for url in hrefs]
    cookies = {cookie['name']: cookie['value'] for cookie in browser.get_cookies()}

    # start_browser(browser, detail_urls[0])
    # for url in detail_urls:
    #     print(url)
    #     start_browser(browser, url)

    browser.quit()
    # return detail_urls, cookies

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,und;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
}
def get_cookies(keyword):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ')
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
    driver.get(index_url)
    time.sleep(30)
    driver.find_element_by_id('keyword').send_keys(keyword)
    time.sleep(5)
    driver.find_element_by_id('btn_query').click()
    time.sleep(20)
    # driver.quit()
    # return detail_urls, cookies

    # set phantomJS's agent to Firefox
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = \
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
    # phantomjsPath = os.getcwd() + "/phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
    # driver = webdriver.PhantomJS(executable_path=phantomjsPath, desired_capabilities=dcap)
    cookie_list = {}
    # driver.get(index_url)
    time.sleep(2)
    cookies = driver.get_cookies()
    for co in cookies:
        if co in cookies:
            if co['name'] == '__jsl_clearance' or co['name'] == '__jsluid':
                cookie_list[co['name']] = co['value']
    driver.quit()
    cookies = requests.utils.add_dict_to_cookiejar(cj=None, cookie_dict=cookie_list)
    print(cookies)
    return cookies

def make_session(url):
    global headers
    cookies = get_cookies('传智播客')
    s = requests.Session()
    # proxy = 'http://' + requests.get(PROXY_POOL_SERVER).text
    # s.proxies = {'http': proxy}
    s.cookies = cookies
    s.headers = headers
    return s

if __name__ == '__main__':
    # 1、requests方法session直接请求
    # plan_request()
    # 2、selenium请求
    # detail_urls, cookies = plan_selenium()
    # for url in detail_urls:
    #     print(url)
    #     start_browser(url, cookies)
    # url = 'http://www.gsxt.gov.cn/%7BDFBB708DB8DD810054A9DABFEBAE3D08F51B8FDBBE5015EA2144718C622221DCAF4104FB3055C1407643C2F4601387E2F3C41FECEE0DED21C219C30FEC2BA5770F7B0F7B0FDDA5D1F480F480F480F480F4037B32E098D126E66284BB286847247035A6176451056E996EBCC89A090A3C570346D5F360635507931224B05ECD99F2057105710571-1540101588770%7D'
    url = 'http://www.gsxt.gov.cn/%7BC1D96EEFA6BF9F624ACBC4DDF5CC236AEB7991B9A0320B883F266FEE7C403FBEB1231A992E37DF226821DC967E719980EDA6018EF06FF343DC7BDD6DF249BB151119111911BFBB309E969E969E969E969E96CF6154508A6860DC4605EAD6859AB28B64A9A6EFC7D05BD0E54B658D703AD240AF87901B131B131B13-1540108139912%7D'
    # url = "http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html"
    data = {
        'draw':'1',
        'start':'0',
        'length':'5'
    }

    s = make_session(url)
    print('准备开始')
    r = s.get(url, verify=False)
    # r = s.post(url, data=data, verify=False)
    print(r)
    print(r.content.decode())
    # 117.136.40.222