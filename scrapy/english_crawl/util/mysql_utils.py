# -*- coding:utf-8 -*-
import MySQLdb



class mysql:
    '''mysql工具类'''

    @staticmethod
    def get_labes(table_name, gmt_create,sub_domain):

        print table_name
        gmt_create = "'" + gmt_create[0:10] + " " + gmt_create[10:18] + "'"
        # print str(gmt_create)[0,10]+" "+str(gmt_create)[10,18]
        base_URL = "https://cn.bing.com/dict/service?q="
        end_URL = '&dtype=sen'
        offset_start = "&offset=0"
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
            name = (row[3].encode("UTF-8"))
            urls.append(base_URL + name + offset_start + end_URL)

        # 关闭数据库连接
        db.close()
        return urls
