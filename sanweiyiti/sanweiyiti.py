#coding:utf-8
import requests
from bs4 import BeautifulSoup 
import time
import sys
sys.path.append('../public/')
import emails

receiver = "xxxxx@cnstrong.cn"
title = "浙江教育考试院更新了三位一体相关内容，请关注"
body = '浙江教育考试院更新了三位一体相关内容，请关注http://www.zjzs.net/moban/index/2c9081f061d15b160161d1653f2e000e_tree.html'
san = '三位一体'
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
url = "http://www.zjzs.net/moban/index/2c9081f061d15b160161d1653f2e000e_list.html"

response = requests.request("GET", url)
#用text中文编码会出现乱码，这里用response.content
soup = BeautifulSoup(response.content,'html.parser')
#判断当日是否有新内容发布，有再判断新内容是否有三位一体相关的内容
today1 = '(' + str(today) + ")"
message = soup.find_all(text= str(today1))
k = len(message)

if message:
	message1 = soup.find_all("a", limit=k)
	print(message1)
	if san in str(message1):
		emails.send_email(receiver,title,body)
	else:
		print("新消息和三位一体无关")
else:
	print("当日没有发布新消息")