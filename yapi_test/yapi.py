#coding:utf-8
'''
YAPI_test，是配合集成在jenkins的接口自动化脚本，用来判断每次测试是否通过，测试失败时发送邮件到项目组提醒
autor:zhjfeng
date:20190219
'''
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = "http://192.168.20.146:3000/api/open/run_auto_test"
querystring = {"id":"158","token":"7708c6969a11f179baf2","mode":"json","email":"false","download":"false"}
#返回json格式化
response = requests.request("GET", url, params=querystring).json()
#print(response)
#提取failednum的值
failedNum = response["message"]["failedNum"]
#print(failedNum)
if failedNum != 0:

	# 第三方 SMTP 服务
	mail_host="smtp.cnstrong.cn"  #设smtp置服务器
	mail_user="fengzhongjie@cnstrong.cn"    #发送邮箱
	mail_pass="xxxxxxxxxx"   #授权码

	sender = 'fengzhongjie@cnstrong.cn'
	receivers = ['eduplan@cnstrong.cn',]  # 收件邮件
	 
	message = MIMEText('20.2有接口执行报错啦，请点击 http://192.168.20.146:3000/api/open/run_auto_test?id=158&token=7708c6969a11f179baf2&mode=html 查看', 'plain', 'utf-8')
	message['From'] = Header("升学规划测试组", 'utf-8')
	message['To'] =  Header("升学规划项目组", 'utf-8')
	 
	subject = '有' + str(failedNum) +'个接口执行报错，请关注'
	message['Subject'] = Header(subject, 'utf-8')

	try:
	    smtpObj = smtplib.SMTP() 
	    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
	    smtpObj.login(mail_user,mail_pass)  
	    smtpObj.sendmail(sender, receivers, message.as_string())
	    print ("测试失败、邮件发送成功")
	except smtplib.SMTPException:
	    print ("Error: 无法发送邮件")

else:
	print("测试通过")



