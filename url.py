#coding:utf-8
#
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup 
import re

url = "http://www.gkzy.com/frontchoose/universitypage.html"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }
#payload = "xname=%E5%9B%9B%E5%B7%9D%E5%A4%A7%E5%AD%A6&area=%E5%85%A8%E5%9B%BD&type=0&attr=0&undefined="

def getschool_id():
	school = "四川大学"
	schoolname = quote(school,'utf-8')
	payload = "xname=" + str(schoolname) + "&area=%E5%85%A8%E5%9B%BD&type=0&attr=0&undefined="
	#print(payload)
	response = requests.request("POST", url, data=payload, headers=headers)
	soup = BeautifulSoup(response.text,'html.parser')
	for link in soup.find_all('a',string = str(school)):	
		url1 = link.get('href')
	if url1.strip()=='':
		pass
	else:
		#rl_b = re.findall(r"(.+?);",url1)
		url_b = re.sub(r';.*$', "", url1)
		return url_b
#print("http://www.gkzy.com" + getschool_id())

response_url = requests.request("GET","http://www.gkzy.com" + getschool_id())
soup_url = BeautifulSoup(response_url.text,'html.parser')
print(soup_url)

'''

def getschool_url():
	response_url = requests.request("GET","http://www.gkzy.com" + getschool_id())
	soup_url = BeautifulSoup(response_url.text,'html.parser')
	print(soup_url)
	for link in soup_url.find_all('a',string = '招生简章'):
		url2 = link.get('href')
		return url2
print(getschool_url())

'''