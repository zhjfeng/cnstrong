#coding:utf-8
'''
author:zhjfeng
date:20190319
'''
import json
import smtplib
import requests

url = "https://share.zaixs.com/wap/community/list"

#page是页数从1开始，每页40条信息
querystring = {"fid":"67","ordertype":"1","page":"2"}
#网站做了防爬，直接发请求会403，这里要在headers里加上User-Agent
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36"
    }
#json格式化
response = requests.request("POST", url, headers=headers, params=querystring).json()
for i in range(0,39):

	tid = response["data"]["list"]["thread"][i]["tid"]
	print(tid)
#print(response)
#


#链接拼接
url = "https://share.zaixs.com/wap/thread/view-thread/tid/661269"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "8ad297fa-fb0a-48db-a9c6-422ddc5cd73d"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)