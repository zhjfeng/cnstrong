#coding:utf-8
import json
import requests
from urllib.parse import quote
'''
删除swagger中pad和m的接口

def get_swagger():
	url = "http://eduplan.leke.cn/v2/api-docs"
	response = requests.request("GET", url) 
	return json.loads(response.text)

def del_swagger_m_hd_py():
	temp = get_swagger()
	paths_new = {k:v for k,v in temp['paths'].items() if '/hd/' not in k and '/m/' not in k}
	temp.update(paths=paths_new)
	return temp

url1 = "http://192.168.20.146:3000/api/interface/add_cat"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjIwOCwiaWF0IjoxNTU0Nzk0NTEwLCJleHAiOjE1NTUzOTkzMTB9.n8MeDSdtquIhAtdGgsfNyX-pmhxileB0L7TaLgpQEuM; _yapi_uid=208",
    }

tag_list = del_swagger_m_hd_py()['tags']
for i in range(len(tag_list)):
	name = tag_list[i]['name']
	desc = tag_list[i]['description']
	#print(name,desc)
	desc_q = quote(desc,'utf-8')
	payload = "desc="+ str(desc_q)+"&name="+str(name)+ "&project_id=358&undefined="
	#payload = "desc=%E5%AD%A6%E9%9C%B8%E8%B0%88%E9%80%9A%E7%94%A8%E5%B0%81%E8%A3%85name=xuebatan-comm-controller&project_id=358&undefined="
	print(payload)	
	response = requests.request("POST", url1, data=payload, headers=headers)
	print(response.text)
'''
import requests

url1 = "http://192.168.20.146:3000/api/interface/add_cat"
url2 = "http://192.168.20.146:3000/api/interface/save"
headers1 = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjIwOCwiaWF0IjoxNTU0Nzk0NTEwLCJleHAiOjE1NTUzOTkzMTB9.n8MeDSdtquIhAtdGgsfNyX-pmhxileB0L7TaLgpQEuM; _yapi_uid=208",
    }
payload1 = "desc=%E5%AD%A6%E9%9C%B8%E8%B0%88%E9%80%9A%E7%94%A8%E5%B0%81%E8%A3%85&name=xuebatan-comm-controller&project_id=358&undefined="
headers2 = {
    'Cookie': "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjIwOCwiaWF0IjoxNTU0Nzk0NTEwLCJleHAiOjE1NTUzOTkzMTB9.n8MeDSdtquIhAtdGgsfNyX-pmhxileB0L7TaLgpQEuM; _yapi_uid=208",
    'Content-Type': "application/json"
    }
response1 = requests.request("POST", url1, data=payload1, headers=headers1)
#response = requests.request("POST", url2, data=payload2, headers=headers2)
cat_id = response1.json()['data']['_id']

payload2 = "{\"method\":\"POST\",\"title\":\"deleteDemandPercent.htm\",\"desc\":\"删除选考科目占比\",\"catname\":\"demand-percent-controller\",\"path\":\"/auth/admin/demandPercent/deleteDemandPercent.htm\",\"req_params\":[],\"req_body_form\":[],\"req_headers\":[],\"req_query\":[{\"name\":\"id\",\"desc\":\"id\",\"required\":\"0\"}],\"req_body_type\":\"json\",\"res_body_type\":\"json\",\"req_body_is_json_schema\":true,\"res_body\":\"{\\n  \\\"type\\\": \\\"object\\\",\\n  \\\"required\\\": [\\n    \\\"code\\\",\\n    \\\"data\\\",\\n    \\\"message\\\"\\n  ],\\n  \\\"properties\\\": {\\n    \\\"code\\\": {\\n      \\\"type\\\": \\\"string\\\",\\n      \\\"description\\\": \\\"200：请求成功；500：请求失败\\\"\\n    },\\n    \\\"currentTime\\\": {\\n      \\\"type\\\": \\\"integer\\\",\\n      \\\"format\\\": \\\"int64\\\"\\n    },\\n    \\\"data\\\": {\\n      \\\"type\\\": \\\"object\\\",\\n      \\\"$$ref\\\": \\\"#/definitions/T\\\"\\n    },\\n    \\\"jsessionid\\\": {\\n      \\\"type\\\": \\\"string\\\",\\n      \\\"description\\\": \\\"sessionid\\\"\\n    },\\n    \\\"message\\\": {\\n      \\\"type\\\": \\\"string\\\",\\n      \\\"description\\\": \\\"默认操作成功；如果操作失败，需要写清楚具体错误信息\\\"\\n    },\\n    \\\"success\\\": {\\n      \\\"type\\\": \\\"boolean\\\",\\n      \\\"example\\\": false,\\n      \\\"description\\\": \\\"请求成功标示\\\"\\n    },\\n    \\\"ticket\\\": {\\n      \\\"type\\\": \\\"string\\\",\\n      \\\"description\\\": \\\"用户身份凭证\\\"\\n    }\\n  },\\n  \\\"description\\\": \\\"接口返回对象\\\",\\n  \\\"$$ref\\\": \\\"#/definitions/Result«T»\\\"\\n}\",\"res_body_is_json_schema\":true,\"project_id\":\"323\",\"catid\":3823,\"dataSync\":\"good\"}"


print(cat_id)