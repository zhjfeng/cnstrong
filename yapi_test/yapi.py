#coding:utf-8
'''
YAPI_test，是配合集成在jenkins的接口自动化脚本，用来判断每次测试是否通过，测试失败时发送邮件到项目组提醒
'''
import requests
import json
import sys
sys.path.append('../public/')
import emails

receiver = "XXXXX@cnstrong.cn"
body = '20.2环境有接口执行报错啦，请点击 http://192.168.20.146:3000/api/open/run_auto_test?id=158&token=7708c6969a11f179baf2&mode=html 查看'
url = "http://192.168.20.146:3000/api/open/run_auto_test"
querystring = {"id":"158","token":"7708c6969a11f179baf2","mode":"json","email":"false","download":"false"}
response = requests.request("GET", url, params=querystring).json()
#print(response)
failedNum = response["message"]["failedNum"]
#print(failedNum)
if (failedNum != 0) and (failedNum != 5):
	title = '有' + str(failedNum) +'个接口执行报错，请关注'
	emails.send_email(receiver,title,body)
else:
	print("测试通过")