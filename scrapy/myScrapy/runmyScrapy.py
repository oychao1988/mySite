from scrapy.cmdline import execute

# execute(['scrapy', 'crawl', 'LagouGETRecruitSpider'])
# execute(['scrapy', 'crawl', 'LagouGETRecruitSpider', '-o', 'positions_data.json'])
def search_position(city, keyword, pageSise):
    execute(['scrapy',
             'crawl',
             'LagouPOSTRecruitSpider',
             # 给spider传参
             '-a', 'city=%s' % city,
             '-a', 'keyword=%s' % keyword,
             '-a', 'pageSize=%d' % pageSise])

search_position('深圳', 'Python', 1)