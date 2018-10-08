from scrapy.cmdline import execute

# execute(['scrapy', 'crawl', 'LagouRecruitSpider'])
execute(['scrapy', 'crawl', 'LagouRecruitSpider', '-o', 'positions_data.json'])