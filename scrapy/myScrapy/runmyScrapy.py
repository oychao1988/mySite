from scrapy.cmdline import execute

# execute(['scrapy', 'crawl', 'LagouGETRecruitSpider'])
# execute(['scrapy', 'crawl', 'LagouGETRecruitSpider', '-o', 'positions_data.json'])
def get_lagou_position(city, keyword, pageSise):
    execute(['scrapy',
             'crawl',
             'LagouPOSTRecruitSpider',
             # 给spider传参
             '-a', 'city=%s' % city,
             '-a', 'keyword=%s' % keyword,
             '-a', 'pageSize=%d' % pageSise])

def get_tencent_position():
    execute(['scrapy',
             'crawl',
             'TencentRecruitCrawlSpider'])


def get_zhilian_position():
    execute(['scrapy',
             'crawl',
             'ZhilianAjaxSpider',
             '-a', 'pages=%d' % 0])

# get_lagou_position('深圳', 'Python', 0)
# get_tencent_position()
get_zhilian_position()