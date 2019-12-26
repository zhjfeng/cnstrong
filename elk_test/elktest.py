#coding:utf-8
'''
elk_test，是抓取ELK平台上，项目组当天报错日志的脚本，如有报错，截取报错数量和信息发送给项目组成员
author:zhjfeng
date:20190301
'''
import requests
import json
import time
import sys
sys.path.append('../public/')
import emails

receiver = "XXXXXX@cnstrong.cn"
url = "http://kibana.leke.cn/elasticsearch/_msearch"
headers = {
    'Content-Type': "application/x-ndjson",
    'kbn-xsrf': "reporting"
    }

#获取查询时间段（当日0点-脚本运行时）传入参数中，getTimeOClockOfToday获取0点时间戳的函数
def getTimeOClockOfToday():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S'))
    return int(time1)
t = time.time()
starttime = getTimeOClockOfToday()*1000
endtime = round(t*1000)

payload = "{\"index\":[\"eduplan_business_log\"]}\r\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"30m\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[\"@timestamp\"],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"error\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":" + str(starttime) + ",\"lte\":" + str(endtime) + ",\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\r\n"
response = requests.request("POST", url, data=payload.encode(), headers=headers).json()
#print(response)
total = response["responses"][0]["hits"]["total"]
date = time.strftime("%Y-%m-%d")

if total != 0:
	message2 = "线上日志报错(抓取了所有包含error的日志信息，未去重），登录http://kibana.leke.cn/app/kibana#/discover，切换至eduplan_business_log，搜索关键字error。 以下为部分报错日志\n"	
	for i in range(0,total):
		#循环输出当天所有报错信息
		message1 = response["responses"][0]["hits"]["hits"][i]["_source"]["message"]
		#print(str(message1)[:100])
		#报错信息取前800个字符
		message2 =message2 + str(i + 1) + '、"message":' +  str(message1)[:400] + "\n"
	body = date + message2 
	title = date +'线上有' + str(total) +'个报错(未去重)，请关注'
	emails.send_email(receiver,title,body)