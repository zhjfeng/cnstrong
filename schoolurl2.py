#coding:utf-8
import requests

url = "http://www.gkzy.com/frontchoose/universitypage.html"
 
payload = "xname=%E6%BD%87%E6%B9%98%E8%81%8C%E4%B8%9A&area=%E5%85%A8%E5%9B%BD&type=0&attr=0&undefined="
#payload = "xname=四川大学&type=0&attr=0&undefined="
#payload_gb2312 = urlencode(payload, encoding='gb2312')
#print(payload_gb2312)
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)