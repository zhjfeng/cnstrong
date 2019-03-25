#coding:utf-8
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup 
import re
import os
import xlrd

url = "http://www.gkzy.com/frontchoose/universitypage.html"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }
#payload = "xname=%E5%9B%9B%E5%B7%9D%E5%A4%A7%E5%AD%A6&area=%E5%85%A8%E5%9B%BD&type=0&attr=0&undefined="
#school = "东莞理工学院"
def getschool_id():
	
	schoolname = quote(school,'utf-8')
	payload = "xname=" + str(schoolname) + "&area=%E5%85%A8%E5%9B%BD&type=0&attr=0&undefined="
	#print(payload)
	
	response = requests.request("POST", url, data=payload, headers=headers)
	soup = BeautifulSoup(response.text,'html.parser')
	try:#部分院校有查询不到的情况，做处理
		for link in soup.find_all('a',string = str(school)):	
			url1 = link.get('href')
			if url1.strip()=='':
				pass
			else:
				#rl_b = re.findall(r"(.+?);",url1)
				url_b = re.sub(r';.*$', "", url1)
				return url_b
	except IndexError:	
		pass	
#print(getschool_id())

def geturl_zs():
	if getschool_id() != None:
		response_url = requests.request("GET","http://www.gkzy.com" + getschool_id())
		#response_url = requests.request("GET","http://www.gkzy.com/college/brief/106.html")
		soup_url = BeautifulSoup(response_url.text, 'html.parser')		
		#找到包含招生简章的节点
		for link in soup_url.find_all(string = str('招生简章')):
			#取到父父节点
			test = link.parent.parent
			#试着取出a标签下的链接，有不存在的情况，做处理
			try:
				url_zs = test.a.get('href')	
				return url_zs
			except AttributeError:
				return school + ' 高考志愿网无数据，需上院校官网查询'
	else:
		return school + ' 高考志愿网无数据，需上院校官网查询'
#print(geturl_zs())
#schoollist = ["四川大学","清华大学"]

excel = xlrd.open_workbook('D:/zsurl.xlsx')
table = excel.sheets()[0]
testurl = table.col_values(0)
for school in testurl:
	#print(school)
	print(geturl_zs())
