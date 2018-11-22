# -*- coding: utf-8 -*-
import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/view/653b9b4ccf84b9d528ea7a2f.html']

    def parse(self, response):
        # print response.xpath('//div').extract()
        pass
