# -*- coding: utf-8 -*-
import re

from imp import reload

import MySQLdb
import scrapy
import sys

from english_crawl.items import EnglishCrawlItem


reload(sys)
sys.setdefaultencoding("utf-8")  # 设置默认编码为utf-8


# bing
class EnglishSpiderSpider(scrapy.Spider):
    name = 'bing_spider'

    def __init__(self, table_name=None, gmt_create=None, domain=None,sub_domain=None, *args, **kwargs):
        super(EnglishSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.get_labels(table_name, gmt_create,sub_domain)
        self.domain = int(domain)
        self.sub_domain = int(sub_domain)

    def get_labels(self, table_name, gmt_create,sub_domain):

        gmt_create = "'" + gmt_create[0:10] + " " + gmt_create[10:18] + "'"
        # print str(gmt_create)[0,10]+" "+str(gmt_create)[10,18]
        base_URL = "https://cn.bing.com/dict/service?q="
        end_URL = '&dtype=sen'
        offset_start = "&offset=0"
        db = MySQLdb.connect("192.168.0.10", "root", "11!!aa", "language_bridge", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        sql = "SELECT * from %s where gmt_create > %s and specialty_id = %s" % (table_name, gmt_create,sub_domain)

        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        urls = []
        for row in results:
            name = (row[3].encode("UTF-8").strip())
            urls.append(base_URL + name + offset_start + end_URL)

        # 关闭数据库连接
        db.close()
        return urls

    def parse(self, response):
        url = response.url
        matchObj = re.match(r'https://cn.bing.com/dict/service\?q=(.*)&offset=(.*)&(.*)', url)
        if matchObj:
            word = matchObj.group(1)
            # 动态定义偏移量，用于获取下一页
            offset = int(matchObj.group(2))
        # https: // cn.bing.com / dict / service\?q = (\S *) & offset =.*
        # 英文单词
        english_sentence = response.xpath("//div[@class='sen_en']")
        # 汉语单词
        chinese_sentence = response.xpath("//div[@class='sen_cn']")
        # 判断是否还有下一页
        is_have_next_page = len(response.xpath("//div[@class='b_pag']")) != 0
        # 组装句子
        english_list = []
        for sub_sentence_en in english_sentence:
            sentence_en = sub_sentence_en.xpath('./span/text() | ./a/text()').extract()
            str_en = "".join(sentence_en)
            english_list.append(str_en)
        chinese_list = []
        for sub_sentence_cn in chinese_sentence:
            sentence_cn = sub_sentence_cn.xpath('./a/text()').extract()
            str_cn = "".join(sentence_cn)
            chinese_list.append(str_cn)
        # 返回数据给管道
        try:
            for sentence_index in range(len(english_list)):
                item = EnglishCrawlItem()
                # item["type"] = word
                item["english"] = english_list[sentence_index]
                item["chinese"] = chinese_list[sentence_index]
                yield item
                # print sub_sentence.xpath('./a/text()').extract()
        except:
            print "编码异常"
            yield item

        # 组装分页url给控制器
        if offset < 1000:
            if is_have_next_page:
                offset += 10
                url = "https://cn.bing.com/dict/service?q=" + word + "&offset=" + str(
                    offset) + '&dtype=sen'
                yield scrapy.Request(url, callback=self.parse)
