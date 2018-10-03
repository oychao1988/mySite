# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentRecruitItme(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    catalog = scrapy.Field()
    recruitNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()
