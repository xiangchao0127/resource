# -*- coding: utf-8 -*-
import re

import MySQLdb
import scrapy

from english_crawl.items import EnglishCrawlItem

# 爱词霸
from english_crawl.util.mysql_utils import mysql


class AicibaSpiderSpider(scrapy.Spider):
    name = 'aiciba_spider'
    print name
    def __init__(self, table_name=None, gmt_create=None, domain=None,sub_domain=None, *args, **kwargs):
        super(AicibaSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.get_labels(table_name,gmt_create,sub_domain)
        self.domain = int(domain)
        self.sub_domain = int(sub_domain)

    def get_labels(self, table_name, gmt_create,sub_domain):

        gmt_create = "'" + gmt_create[0:10] + " " + gmt_create[10:18] + "'"
        base_URL = "http://dj.iciba.com/"
        end_URL = "-%01-0-0.html"
        offset_start = 1
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
            urls.append(base_URL + name +"-1-"+ str(offset_start) + end_URL)

        # 关闭数据库连接
        db.close()
        return urls

    def parse(self, response):
        url = response.url
        matchObj = re.match(r'http://dj.iciba.com/(.*)-1-(.*)-%01-0-0.html', url)
        if matchObj:
            word = matchObj.group(1)
            # 动态定义偏移量，用于获取下一页
            offset = int(matchObj.group(2))
        # 判断是否还有下一页
        is_have_next_page = len(response.xpath("//li[@class='dj_li']").extract()) == 10
        sentences = response.xpath("//li[@class='dj_li']")
        for sentence in sentences:
           try:
            english = sentence.xpath("./p[@class='stc_en']/span[2]/@con").extract()[0]
            chinese = sentence.xpath("./p[@class='stc_cn']/span[2]/@con").extract()[0]
            item = EnglishCrawlItem()
            item["english"] = english
            item["chinese"] = chinese
            yield item
           except:
               pass
            # 组装分页url给控制器
        if offset < 50:
            if is_have_next_page:
                offset += 1
                url = "http://dj.iciba.com/" + word + "-1-" + str(offset) + '-%01-0-0.html'
                yield scrapy.Request(url, callback=self.parse)
