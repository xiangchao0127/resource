# -*- coding: utf-8 -*-


import codecs
import jieba
from english_crawl.util import pdf_parse

# 结巴分词器


seg_list = jieba.cut('邓超,1979年出生于江西南昌,中国内地男演员、电影导演、投资出品人、互联网投资人。')

f1 = codecs.open("d2w_ltp.txt", "w")
# print "/".join(seg_list)

for i in seg_list:
    str1 = i.encode("utf-8")
    if str1 != "," and str1 != "。" and str1 != "、":
        f1.write(str1)
        f1.write(str(" "))
pdf_parse.Pdf2Txt()
f1.close()
