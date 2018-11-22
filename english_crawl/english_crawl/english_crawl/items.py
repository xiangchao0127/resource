# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    #英文句子
    english = scrapy.Field()
    #中文句子
    chinese = scrapy.Field()



