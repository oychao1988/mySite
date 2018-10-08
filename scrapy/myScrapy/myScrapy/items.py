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


class LagouRecruitItem(scrapy.Item):
    category = scrapy.Field()  # 工作类别
    category_url = scrapy.Field()  # 类别url

    adWord = scrapy.Field()
    appShow = scrapy.Field()
    approve = scrapy.Field()
    businessZones = scrapy.Field()  # 商业区域
    city = scrapy.Field()  # 城市
    companyFullName = scrapy.Field()  # 公司全称
    companyId = scrapy.Field()
    companyLabelList = scrapy.Field()  # 公司标签列表
    companyLogo = scrapy.Field()  # 公司logo
    companyShortName = scrapy.Field()  # 公司简称
    companySize = scrapy.Field()  # 公司规模
    createTime = scrapy.Field()  # 发布时间
    deliver = scrapy.Field()
    district = scrapy.Field()  # 地区
    education = scrapy.Field()  # 学历
    explain = scrapy.Field()
    financeStage = scrapy.Field()  # 融资阶段
    firstType = scrapy.Field()  # 工作类型1
    formatCreateTime = scrapy.Field()
    gradeDescription = scrapy.Field()
    hitags = scrapy.Field()
    imState = scrapy.Field()
    industryField = scrapy.Field()
    industryLables = scrapy.Field()
    isSchoolJob = scrapy.Field()
    jobNature = scrapy.Field()
    lastLogin = scrapy.Field()
    linestaion = scrapy.Field()
    latitude = scrapy.Field()  # 纬度
    longitude = scrapy.Field()  # 经度
    pcShow = scrapy.Field()
    plus = scrapy.Field()
    positionAdvantage = scrapy.Field()  # 职位优势
    positionId = scrapy.Field()
    positionLables = scrapy.Field()  # 职位标签
    positionName = scrapy.Field()  # 职位名称
    promotionScoreExplain = scrapy.Field()
    publisherId = scrapy.Field()  # 职位编号
    resumeProcessDay = scrapy.Field()
    resumeProcessRate = scrapy.Field()
    salary = scrapy.Field()  # 薪资
    score = scrapy.Field()
    secondType = scrapy.Field()  # 工作类型2
    skillLables = scrapy.Field()  # 技能标签
    stationname = scrapy.Field()  # 站点名称
    subwayline = scrapy.Field()  # 地铁线路
    thirdType = scrapy.Field()  # 工作类型3
    workYear = scrapy.Field()  # 工作年限