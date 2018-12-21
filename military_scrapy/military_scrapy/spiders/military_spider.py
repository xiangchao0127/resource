# -*- coding: utf-8 -*-
import re

import scrapy

from military_scrapy.items import MilitaryScrapyItem


class MilitarySpiderSpider(scrapy.Spider):
    name = 'military_spider'
    allowed_domains = ['dict.biomart.cn']

    with open('D:\military\military_scrapy\military_scrapy\spiders\words1', 'r') as f1:
        results = f1.readlines()
    # start_urls = ['http://dict.biomart.cn/sentence.htm?wd=%E5%BF%83%E8%84%8F&p=1']
    urls = []
    for row in results:
        word = (row.strip())
        urls.append("http://dict.biomart.cn/sentence.htm?wd=" + word + "&p=1")
    start_urls = set(urls)

    def parse(self, response):
        url = response.url
        matchObj = re.match('http://dict.biomart.cn/sentence.htm\?wd=(.*)&p=(.*)', url)
        if matchObj:
            word = matchObj.group(1)
            # 动态定义偏移量，用于获取下一页
            offset = int(matchObj.group(2))
        page_size = len(response.xpath("//div[@class='page_A']/text()").extract())
        is_have_next_page = None
        if(page_size!=0):
        #页码信息
         page_content = response.xpath("//div[@class='page_A']/text()").extract()[page_size-1]
         strs = page_content.split(',')[1]
        #获取总页数
         size = int(strs[0:len(strs)-3])
         is_have_next_page = int(offset) < size
        sentences = response.xpath("//li[@class='word_it1']")
        for line in sentences:
             item = MilitaryScrapyItem()
             extract_chinese = line.xpath("./p[1]/text()|./p[1]/b/text()").extract()
             chinese_str = "".join(extract_chinese)
             print  chinese_str
             item["chinese"] = chinese_str
             extract_english = line.xpath("./p[2]/text()").extract()
             english_str = "".join(extract_english)
             print  extract_english[0]
             item["english"] = english_str
             yield item

        if is_have_next_page:
            offset += 1
            url = "http://dict.biomart.cn/sentence.htm?wd=" + word + "&p=" + str(
                offset)
            yield scrapy.Request(url, callback=self.parse)