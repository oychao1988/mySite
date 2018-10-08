import scrapy
from myScrapy.items import LagouRecruitItem
from urllib.parse import urlencode


class LagouRecruitSpider(scrapy.spiders.Spider):
    name = 'LagouRecruitSpider'
    start_urls = ['https://www.lagou.com']
    allowed_domains = ['lagou.com']

    # cookie = {"user_trace_token": "20181003162424-bc2e8234-c6e5-11e8-a8cf-525400f775ce",
    #           "LGUID": "20181003162424-bc2e8853-c6e5-11e8-a8cf-525400f775ce",
    #           "index_location_city": "%E6%B7%B1%E5%9C%B3",
    #           "WEBTJ-ID": "20181008082215-166510d9256373-0c1c9d5e3a71e-3e70055f-1049088-166510d925740e",
    #           "JSESSIONID": "ABAAABAAADEAAFI2AA9D579308DA2197B701A300CA7B0A0",
    #           "_gat": "1",
    #           "PRE_UTM": "",
    #           "PRE_HOST": "",
    #           "PRE_SITE": "https%3A%2F%2Fwww.lagou.com%2F",
    #           "PRE_LAND": "https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel",
    #           "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1538555064,1538555073,1538958136,1538958145",
    #           "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1538977472",
    #           "LGSID": "20181008134234-f4d3c122-cabc-11e8-a9c8-525400f775ce",
    #           "LGRID": "20181008134432-3adec7ea-cabd-11e8-bb68-5254005c3644",
    #           "_ga": "GA1.2.1686656861.1538555064",
    #           "_gid": "GA1.2.1131033380.1538975278",
    #           "TG-TRACK-CODE": "index_navigation",
    #           "SEARCH_ID": "daec0ec00dc34b6bab27f61734e6a6c3"}

    cookie = {"user_trace_token": "20181003162424-bc2e8234-c6e5-11e8-a8cf-525400f775ce",
              "LGUID": "20181003162424-bc2e8853-c6e5-11e8-a8cf-525400f775ce",
              "index_location_city": "%E6%B7%B1%E5%9C%B3",
              "WEBTJ-ID": "20181008082215-166510d9256373-0c1c9d5e3a71e-3e70055f-1049088-166510d925740e",
              "JSESSIONID": "ABAAABAAADEAAFI2AA9D579308DA2197B701A300CA7B0A0",
              "sajssdk_2015_cross_new_user": "1",
              "_gid": "GA1.2.1131033380.1538975278",
              "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22166527cbe742a0-094a56f8fc244b-3e70055f-1049088-166527cbe762e7%22%2C%22%24device_id%22%3A%22166527cbe742a0-094a56f8fc244b-3e70055f-1049088-166527cbe762e7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
              "TG-TRACK-CODE": "index_navigation",
              "SEARCH_ID": "cc9815a533da419bbb9990073746e4ec",
              "X_HTTP_TOKEN": "84a16a5dc6d5de3f8be58743a2b0fe71",
              "_ga": "GA1.2.1686656861.1538555064",
              "_gat": "1",
              "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1538555064,1538555073,1538958136,1538958145",
              "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1538987200",
              "LGSID": "20181008154911-a4fbf00b-cace-11e8-bb68-5254005c3644",
              "LGRID": "20181008162641-e24a863e-cad3-11e8-bb68-5254005c3644"}

    # def start_requests(self):
    #     url = 'https://www.lagou.com/jobs/positionAjax.json?'
    #     print('*****************start_reqeusts*******************')
    #     lagouHeaders = {"Accept": "application/json,text/javascript, */*;q=0.01",
    #                     "Accept-Encoding": "gzip, deflate",
    #                     "Accept-Language": "zh-CN,zh;q=0.8",
    #                     "Connection": "keep-alive",
    #                     "Content-Length": "25",
    #                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #                     "Host": "www.lagou.com",
    #                     "Origin": "https://www.lagou.com",
    #                     "Referer": "https://www.lagou.com/jobs/list_Python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=",
    #                     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    #                     "X-Anit-Forge-Code": "0",
    #                     "X-Anit-Forge-Token": "None",
    #                     "X-Requested-With": "XMLHttpRequest",
    #                     "Cookie": "user_trace_token=20181003162424-bc2e8234-c6e5-11e8-a8cf-525400f775ce; LGUID=20181003162424-bc2e8853-c6e5-11e8-a8cf-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; WEBTJ-ID=20181008082215-166510d9256373-0c1c9d5e3a71e-3e70055f-1049088-166510d925740e; _ga=GA1.2.1686656861.1538555064; LGRID=20181008094549-e23ae91a-ca9b-11e8-a9b6-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538555064,1538555073,1538958136,1538958145; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538963150; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAADEAAFI2AA9D579308DA2197B701A300CA7B0A0; SEARCH_ID=8b7a47b35f3947598ed46b6b0aecee01"
    #                     }
    #
    #     query_params = urlencode({"city": "深圳",
    #                     "needAddtionalResult": "false"})
    #
    #     form_datas = {"first": "true",
    #                   "pn": "1",
    #                   "kd": "人工智能"}
    #
    #     yield scrapy.FormRequest(url=url + query_params,
    #                              headers=lagouHeaders,
    #                              method='POST',
    #                              formdata=form_datas,
    #                              callback=self.parse
    #                              )

    def parse(self, response):
        for item in response.xpath('//div[@class="menu_box"]/div/dl/dd/a'):
            category = item.xpath('text()').extract()
            category_url = item.xpath('@href').extract_first()

            RecruitItem = LagouRecruitItem()
            RecruitItem['category'] = category
            RecruitItem['category_url'] = category_url

            # 粗暴的添加分页
            for i in range(30):
                try:
                    category_sub_url = category_url + str(i+1)
                    yield scrapy.Request(url=category_sub_url, cookies=self.cookie, callback=self.parse_url)
                except:
                    pass

            # yield RecruitItem

    def parse_url(self, response):
        login_url = 'https://passport.lagou.com/login/login.html?msg=validation&uStatus=2&clientIp=183.237.64.70'
        if response.url != login_url:
            print('response.url =', response.url)
            for sel in response.xpath('//ul[@class="item_con_list"]/li'):
                try:
                    # adWord = scrapy.Field()
                    # appShow = scrapy.Field()
                    # approve = scrapy.Field()
                    # businessZones = scrapy.Field()  # 商业区域
                    # city = scrapy.Field()  # 城市
                    companyFullName = sel.xpath('div/div/div/a/text()').extract()[-1]  # 公司全称
                    # companyId = scrapy.Field()
                    # companyLabelList = scrapy.Field()  # 公司标签列表
                    # companyLogo = scrapy.Field()  # 公司logo
                    # companyShortName = scrapy.Field()  # 公司简称
                    # companySize = scrapy.Field()  # 公司规模
                    createTime = sel.xpath('div/div/div/span/text()').extract()[0]  # 发布时间
                    # deliver = scrapy.Field()
                    # district = scrapy.Field()  # 地区
                    education = sel.xpath('div[1]/div[1]/div[2]/div/text()').extract()[-1].split(' / ')[-1].split('\n')[0]  # 学历
                    # explain = scrapy.Field()
                    # financeStage = scrapy.Field()  # 融资阶段
                    # firstType = scrapy.Field()  # 工作类型1
                    # formatCreateTime = scrapy.Field()
                    # gradeDescription = scrapy.Field()
                    # hitags = scrapy.Field()
                    # imState = scrapy.Field()
                    # industryField = scrapy.Field()
                    # industryLables = scrapy.Field()
                    # isSchoolJob = scrapy.Field()
                    # jobNature = scrapy.Field()
                    # lastLogin = scrapy.Field()
                    # linestaion = scrapy.Field()
                    # latitude = scrapy.Field()  # 纬度
                    # longitude = scrapy.Field()  # 经度
                    # pcShow = scrapy.Field()
                    # plus = scrapy.Field()
                    positionAdvantage = sel.xpath('div[2]/div[1]/span/text()').extract()  # 职位优势
                    # positionId = scrapy.Field()
                    # positionLables = scrapy.Field()  # 职位标签
                    positionName = sel.xpath('div/div/div/a/h3/text()').extract()[0]  # 职位名称
                    # promotionScoreExplain = scrapy.Field()
                    # publisherId = scrapy.Field()  # 职位编号
                    # resumeProcessDay = scrapy.Field()
                    # resumeProcessRate = scrapy.Field()
                    salary = sel.xpath('div/div/div/div/span/text()').extract()[0]  # 薪资
                    # score = scrapy.Field()
                    # secondType = scrapy.Field()  # 工作类型2
                    # skillLables = scrapy.Field()  # 技能标签
                    # stationname = scrapy.Field()  # 站点名称
                    # subwayline = scrapy.Field()  # 地铁线路
                    # thirdType = scrapy.Field()  # 工作类型3
                    workYear = sel.xpath('div[1]/div[1]/div[2]/div/text()').extract()[-1].split(' / ')[0]  # 工作年限

                    position_item = LagouRecruitItem()
                    position_item['companyFullName'] = companyFullName
                    position_item['createTime'] = createTime
                    position_item['education'] = education
                    position_item['positionAdvantage'] = positionAdvantage
                    position_item['positionName'] = positionName
                    position_item['salary'] = salary
                    position_item['workYear'] = workYear

                    yield position_item
                except Exception:
                    continue