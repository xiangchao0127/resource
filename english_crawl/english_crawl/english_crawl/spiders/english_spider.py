# -*- coding: utf-8 -*-
import re
import time

import scrapy
import sys

from english_crawl.items import EnglishCrawlItem

reload(sys)
sys.setdefaultencoding("utf-8")  # 设置默认编码为utf-8


class EnglishSpiderSpider(scrapy.Spider):
    name = 'english_spider'
    allowed_domains = ['cn.bing.com']
    # 定义偏移量，用于获取下一页
    offset = 0
    # 关键字
    keyword = '今天'
    list_key_word = ['物理', '化学', '语文', '数学', '英语', '生物', '自然', '地理', '政治']
    base_URL = "https://cn.bing.com/dict/service?q=" + keyword + "&offset="
    end_URL = '&dtype=sen&&qs=n&form=Z9LH5&sp=-1&pq=' + keyword + '&sc=8-2&sk=&cvid=93A8F03149F64A7899E591C107A76A16'

    start_urls = []
    for key_word in list_key_word:
        start_urls.append(
            "https://cn.bing.com/dict/service?q=" + key_word + "&offset=" + '&dtype=sen&&qs=n&form=Z9LH5&sp=-1&pq=' + key_word + '&sc=8-2&sk=&cvid=93A8F03149F64A7899E591C107A76A16')

    # start_urls = ['https://cn.bing.com/dict/search?q=物理']

    def parse(self, response):
        word = ""
        url = response.url
        matchObj = re.match(r'https://cn.bing.com/dict/service\?q=(\S*)&offset=.*', url)
        if matchObj:
            word = matchObj.group(1)
        # https: // cn.bing.com / dict / service\?q = (\S *) & offset =.*
        # 英文单词
        english_sentence = response.xpath("//div[@class='sen_en']")
        # 汉语单词
        chinese_sentence = response.xpath("//div[@class='sen_cn']")
        print "==================="
        # 判断是否还有下一页
        is_have_next_page = len(response.xpath("//div[@class='b_pag']")) == 0
        print is_have_next_page
        # time.sleep(1)
        # 组装句子
        english_list = []
        for sub_sentence in english_sentence:
            sentence = sub_sentence.xpath('./span/text() | ./a/text()').extract()
            str1 = "".join(sentence)
            english_list.append(str1)
        chinese_list = []
        for sub_sentence in chinese_sentence:
            sentence = sub_sentence.xpath('./a/text()').extract()
            str1 = "".join(sentence)
            chinese_list.append(str1)
        # 返回数据给管道
        for sentence_index in range(len(english_list)):
            item = EnglishCrawlItem()
            item["english"] = english_list[sentence_index]
            item["chinese"] = chinese_list[sentence_index]
            print(item["chinese"])
            yield item
            # print sub_sentence.xpath('./a/text()').extract()

        # 组装分页url给控制器
        if self.offset < 1000:
            if is_have_next_page:
                pass
                return
            self.offset += 10
            url = "https://cn.bing.com/dict/service?q=" + word + "&offset=" + str(
                self.offset) + '&dtype=sen&&qs=n&form=Z9LH5&sp=-1&pq=' + word + '&sc=8-2&sk=&cvid=93A8F03149F64A7899E591C107A76A16'
            yield scrapy.Request(url, callback=self.parse)
