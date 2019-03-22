# -*- coding: utf-8 -*-

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
'''
import os
import xlrd
import requests
from bs4 import BeautifulSoup
import re

schoolurl = eval(open('D:/test.txt','r').read())
#print(schoolurl)

for key,value in schoolurl.items():
    try:
        response = requests.request("GET", value, timeout=5)
        soup = BeautifulSoup(response.content,'html.parser')
        a = soup.find_all("a", text=re.compile("招生"))
        print('\n' + key)
        for link in a:
            url_id = link.get('href')
            print(url_id)
    except:
        print(key + "请求报错")
'''
