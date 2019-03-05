#coding:utf-8
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

#获取查询时间段（当日0点-脚本运行时）传入参数中，getTimeOClockOfToday获取0点时间戳的函数
def getTimeOClockOfToday():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S'))
    return int(time1)

t = time.time()
starttime = getTimeOClockOfToday()*1000
endtime = round(t*1000)

url = "http://kibana.leke.cn/elasticsearch/_msearch"
payload = "{\"index\":[\"eduplan_business_log\"]}\r\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"30m\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[\"@timestamp\"],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"error\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":" + str(starttime) + ",\"lte\":" + str(endtime) + ",\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\r\n"
#payload = "{\"index\":[\"eduplan_business_log\"],\"ignore_unavailable\":true,\"preference\":1551507606271}\r\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"30m\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[\"@timestamp\"],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"异常\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":1551421208215,\"lte\":1551507608216,\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\r\n"
#print(payload)
headers = {
    'Content-Type': "application/x-ndjson",
    'kbn-xsrf': "reporting"
    }

response = requests.request("POST", url, data=payload.encode(), headers=headers).json()
#print(response)
total = response["responses"][0]["hits"]["total"]
date = time.strftime("%Y-%m-%d")

if total != 0:
	# 第三方 SMTP 服务	
	mail_host="smtp.cnstrong.cn"  #设smtp置服务器
	mail_user="xxxxxxxxxxxx@cnstrong.cn"    #发送邮箱
	mail_pass="xxxxxxx"   #授权码

	sender = 'xxxxxxxx@cnstrong.cn'
	receivers = ['xxxxxx@cnstrong.cn',]  # 收件邮件
	message2 = "线上日志报错(抓取了所有包含error的日志信息，未剃重），登录http://kibana.leke.cn/app/kibana#/discover，切换至eduplan_business_log，搜索关键字error。 以下为部分报错日志\n"	
	for i in range(0,total):
		#循环输出当天所有报错信息
		message1 = response["responses"][0]["hits"]["hits"][i]["_source"]["message"]
		#print(str(message1)[:100])
		#报错信息取前800个字符
		message2 =message2 + str(i + 1) + '、"message":' +  str(message1)[:400] + "\n"

	message = MIMEText(date + message2, 'plain', 'utf-8')
	message['From'] = Header("升学规划测试组", 'utf-8')
	message['To'] =  Header("升学规划项目组", 'utf-8')
 
	subject = date +'线上有' + str(total) +'个报错，请关注'
	message['Subject'] = Header(subject, 'utf-8')
	#print(message2)

	try:
	    smtpObj = smtplib.SMTP() 
	    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
	    smtpObj.login(mail_user,mail_pass)  
	    smtpObj.sendmail(sender, receivers, message.as_string())
	    print ("当天线上有报错，邮件发送成功")
	except smtplib.SMTPException:
	    print ("Error: 当天线上有报错，无法发送邮件")

else:
	print("测试通过")
