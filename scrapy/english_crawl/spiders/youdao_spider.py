# -*- coding: utf-8 -*-
import re
import sys

import MySQLdb
import scrapy

from english_crawl.items import EnglishCrawlItem

reload(sys)
sys.setdefaultencoding("utf-8")  # 设置默认编码为utf-8


# 有道
class YoudaoSpiderSpider(scrapy.Spider):
    name = 'youdao_spider'
    allowed_domains = ['youdao.com']

    def __init__(self, table_name=None, gmt_create=None, domain=None, sub_domain=None, *args, **kwargs):
        super(YoudaoSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.get_labels(table_name, gmt_create,sub_domain)
        self.domain = int(domain)
        self.sub_domain = int(sub_domain)

    def get_labels(self, table_name, gmt_create,sub_domain):

        gmt_create = "'" + gmt_create[0:10] + " " + gmt_create[10:18] + "'"
        # print str(gmt_create)[0,10]+" "+str(gmt_create)[10,18]
        base_URL = 'http://www.youdao.com/example/'

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
            urls.append(base_URL + name)

        # 关闭数据库连接
        db.close()
        return urls

    def parse(self, response):
        url = response.url
        matchObj = re.match(r'http://www.youdao.com/example/(.*)', url)
        enmode = re.compile(u'^[a-zA-Z]')
        if matchObj:
            word = matchObj.group(1)
            is_english = enmode.search(word)
        sentences = response.xpath("//ul[@class='ol']/li")
        english_list = []
        chinese_list = []
        for sentence in sentences:
            chinese = sentence.xpath("./p[2]/span/text()").extract()
            cn = "".join(chinese)
            chinese_list.append(cn)
            english = sentence.xpath("./p[1]/span/text() | ./p[1]/span/b/text()").extract()
            en = "".join(english)
            english_list.append(en)
            # print chinese_list
        try:
            for sentence_index in range(len(english_list)):
                item = EnglishCrawlItem()
                if is_english:
                  item["english"] = english_list[sentence_index]
                  item["chinese"] = chinese_list[sentence_index]
                else:
                  item["english"] = chinese_list[sentence_index]
                  item["chinese"] = english_list[sentence_index]
                yield item
                # print sub_sentence.xpath('./a/text()').extract()
        except:
            print "编码异常"
            yield item
