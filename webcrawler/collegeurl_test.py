# -*- coding: utf-8 -*-
'''
检测招生和院校官网的死链接
'''
import os
import xlrd
import requests

excel = xlrd.open_workbook('D:/url.xlsx')
table = excel.sheets()[0]
testurl = table.col_values(2)
#testurl = ['http://www.whu.edu.cn', 'http://210.34.80.109/zsb/']
for url in testurl:
    try:
        response = requests.request("GET", url, timeout=5)
        #print(response.status_code)
        if response.status_code != 200:
            print(url + '请求失败')
    except :
        print(url + '请求失败')