# -*- coding: utf-8 -*-
import re

import MySQLdb
import scrapy

# 句酷
from english_crawl.items import EnglishCrawlItem


class JukuSpiderSpider(scrapy.Spider):
    name = 'juku_spider'
    allowed_domains = ['jukuu.com']

    def __init__(self, table_name=None, gmt_create=None, domain=None, sub_domain=None, *args, **kwargs):
        super(JukuSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.get_labels(table_name, gmt_create,sub_domain)
        self.domain = int(domain)
        self.sub_domain = int(sub_domain)

    def get_labels(self, table_name, gmt_create,sub_domain):

        gmt_create = "'" + gmt_create[0:10] + " " + gmt_create[10:18] + "'"
        # print str(gmt_create)[0,10]+" "+str(gmt_create)[10,18]
        base_URL = 'http://www.jukuu.com/show-'
        end_URL = '-0.html'

        db = MySQLdb.connect("192.168.0.10", "root", "11!!aa", "language_bridge", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        sql = "SELECT * from %s where gmt_create > %s and specialty_id = %s" % (table_name, gmt_create, sub_domain)

        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        urls = []
        for row in results:
            name = (row[3].encode("UTF-8").strip())
            urls.append(base_URL + name  + end_URL)

        # 关闭数据库连接
        db.close()
        return urls

    def parse(self, response):
        url = response.url
        matchObj = re.match(r'http://www.jukuu.com/show-(.*)-(.*).html', url)
        if matchObj:
            word = matchObj.group(1)
            # 动态定义偏移量，用于获取下一页
            offset = int(matchObj.group(2))

        # 判断是否还有下一页
        is_have_next_page = "下一页" in response.xpath("//p[@align='center']/a/text()").extract()
        english_list = response.xpath("//table[@width='680']/tr[@class='e']")
        chinese_list = response.xpath("//table[@width='680']/tr[@class='c']")
        english_sentence = []
        chinese_sentence = []

        for english in english_list:
            english_str_list = english.xpath("./td[2]/text() | td[2]/b/text()").extract()
            english_str = "".join(english_str_list)
            english_sentence.append(english_str)

        for chinese in chinese_list:
            chinese_str_list = chinese.xpath("./td[2]/text() | td[2]/b/text()").extract()
            chinese_str = "".join(chinese_str_list)
            chinese_sentence.append(chinese_str)

        for sentence_index in range(len(english_sentence)):
            item = EnglishCrawlItem()
            # item["type"] = word
            item["english"] = english_sentence[sentence_index]
            item["chinese"] = chinese_sentence[sentence_index]
            yield item

        if offset < 50:
            if is_have_next_page:
                offset += 1
                url = "http://www.jukuu.com/show-" + word + "-" + str(
                    offset) + '.html'
                yield scrapy.Request(url, callback=self.parse)
