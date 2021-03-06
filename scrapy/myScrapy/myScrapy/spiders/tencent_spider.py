import re

import scrapy

from myScrapy.items import TencentRecruitItme


class TencentRecruitSpider(scrapy.spiders.Spider):
    name = 'TencentRecruitSpider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        # 保存网页
        # with open('TencentRecruit.txt', 'wb') as f:
        #     f.write(response.body)

        # 提取网页数据
        for sel in (response.xpath('//*[@class="even"]')+response.xpath('//*[@class="odd"]')):
            name = sel.xpath('./td[1]/a/text()').extract()[0]
            detailLink = sel.xpath('./td[1]/a/@href').extract()[0]
            catalog = None
            if sel.xpath('./td[2]/text()'):
                catalog = sel.xpath('./td[2]/text()').extract()[0]
            recruitNumber = sel.xpath('./td[3]/text()').extract()[0]
            workLocation = sel.xpath('./td[4]/text()').extract()[0]
            publishTime = sel.xpath('./td[5]/text()').extract()[0]

            # 打印提取的数据
            # print('*'*50)
            # print(name, detailLink, catalog, recruitNumber, workLocation, publishTime)

            item = TencentRecruitItme()
            item['name'] = name
            item['detailLink'] = detailLink
            if catalog:
                item['catalog'] = catalog
            item['recruitNumber'] = recruitNumber
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime

            yield item

        nextFlag = response.xpath('//*[@id="next"]/@href')[0].extract()
        if 'start' in  nextFlag:
            curpage = re.search('(\d+)', response.url).group(1)
            page = int(curpage) + 10
            url = re.sub('(\d+)', str(page), response.url)
            print(url)
            yield scrapy.Request(url, callback=self.parse)