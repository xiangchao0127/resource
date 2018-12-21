# -*- coding: utf-8 -*-
import random
from time import sleep

import requests
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from lxml import etree

class spider:
    def __init__(self):
        self.es = Elasticsearch(host="192.168.0.10", port=9200, timeout=5000)
    def get_english(self,url):
        # 要访问的目标HTTPS页面
        # targetUrl = "https://httpbin.org/ip"

        # 代理服务器
        proxyHost = "p5.t.16yun.cn"
        proxyPort = "6445"

        # 代理隧道验证信息
        proxyUser = "16LLJHES"
        proxyPass = "546239"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        # 设置 http和https访问都是用HTTP代理
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        #  设置IP切换头
        tunnel = random.randint(1, 10000)
        headers = {"Proxy-Tunnel": str(tunnel)}

        resp = requests.get(url, proxies=proxies, headers=headers)
        # response = requests.get(url)
        sourceHtml = resp.text

        selector = etree.HTML(sourceHtml)
        sentences = selector.xpath("//li[@class='word_it1']")
        i = 0
        docs = []
        for line in sentences:
            extract_chinese = line.xpath("./p[1]/text()|./p[1]/b/text()")
            chinese_str = "".join(extract_chinese)
            print  chinese_str
            extract_english = line.xpath("./p[2]/text()")
            english_str = "".join(extract_english)
            i += 1
            print i
            print  english_str
            doc = {
                "_index": "en-us",
                "_type": "data",
                "_source": {
                    "domain": 200,
                    "sub_domain": 250,
                    "chinese": chinese_str,
                    "english": english_str
                }
            }
            docs.append(doc)
        bulk(self.es, docs, index="en-us", raise_on_error=True)

    def xunhuan(self,words):
        for i in range(1, 3):
            url = "http://dict.biomart.cn/sentence.htm?wd=" + words + "&p=" + str(i)
            self.get_english(url)

    def run(self):
        with open('D:\military\military_scrapy\military_scrapy\spiders\words', 'r') as f1:
            results = f1.readlines()

        urls = []
        for row in results:
            word = (row.strip())
            urls.append(word)
        start_urls = set(urls)
        # params.append("heart")
        for i in start_urls:
            self.xunhuan(i)

if __name__ == '__main__':
        spider = spider()
        spider.run()





