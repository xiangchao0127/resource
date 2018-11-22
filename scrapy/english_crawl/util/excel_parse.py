# -*- coding: utf-8 -*-

import xlrd
xlrd.Book.encoding = "utf-8"
workbook = xlrd.open_workbook(u'20180531药品数据库.xlsx')

sheet_names = workbook.sheet_names()
names = []
numbers = 0
for sheet_name in sheet_names:
    sheet2 = workbook.sheet_by_name(sheet_name)

    for i in sheet2.get_rows():
        if numbers == 0:
            numbers += 1
            continue
        print names.append(i[7].value.encode("utf-8"))


setNames = set(names)
print len(setNames)
filename = open("file","w")
for i in setNames:
    print i

