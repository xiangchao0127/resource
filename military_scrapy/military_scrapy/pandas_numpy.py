# -*- coding: utf-8 -*-
import pandas as pd

excel = pd.read_excel("military.xlsx", sheet_name=0)
e = excel["key"]
# out = pd.ExcelWriter('output.xlsx')
e.to_excel("output.xlsx")
# out.save()


