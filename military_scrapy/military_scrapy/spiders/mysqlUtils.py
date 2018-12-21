# -*- coding: utf-8 -*-
import re

import MySQLdb
# print str(gmt_create)[0,10]+" "+str(gmt_create)[10,18]

db = MySQLdb.connect("192.168.0.10", "root", "11!!aa", "language_bridge", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# agriculture
# electricity
# information
# infrastructure
# manufacture
# medicine
# military
# military_new
# petrochemical_corporation
# traffic
sql = "SELECT * from traffic"

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
urls = []
for row in results:
    name = (row[3].encode("UTF-8").strip())
    if re.match(u"[\u4e00-\u9fa5]+",name.decode("utf-8")):
     print name

# 关闭数据库连接
db.close()



