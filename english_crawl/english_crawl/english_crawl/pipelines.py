# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class EnglishCrawlPipeline(object):
    def __init__(self):
        self.file = open("tess", "w")

    def process_item(self, item, spider):
        self.file.write(item['english'] + "\n")
        self.file.write(item['chinese']+"\n\n")
        return item


    def close_spider(self):
        self.file.close()
