# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk




class EnglishCrawlPipeline(object):
    def __init__(self):
        self.es = Elasticsearch(host = "192.168.0.10",port = 9200,timeout=5000)
        self.docs = []


    def process_item(self, item, spider):

        doc = {
            "_index": "en-us",
            "_type": "data",
            "_source": {
            "domain": spider.domain,
            "sub_domain": spider.sub_domain,
            "chinese": item['chinese'],
            "english": item['english']
            }
        }
        self.docs.append(doc)
        return item

    def close_spider(self,spider):

        count = 0
        success, _ = bulk(self.es, self.docs, index="en-us", raise_on_error=True)
        count += success
        print("insert %s lines" % count)
