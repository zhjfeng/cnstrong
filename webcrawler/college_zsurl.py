#coding:utf-8
'''
爬取院校官网中和招生相关的链接
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
