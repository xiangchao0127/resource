from scrapy.cmdline import execute
execute('scrapy crawl youdao_spider -a table_name=military_new -a gmt_create=2018-09-2815:00:00 -a domain=101 -a sub_domain=103'.split())