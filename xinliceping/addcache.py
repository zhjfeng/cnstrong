#coding:utf-8
import requests
import json
'''
#该接口为获取当前专业数量
url = "https://eduplan.leke.cn/auth/student/forecast/profession/getCollegeAndMajorNum.htm"
payload = "{\"objectId\":\"5ca2ce665db0dc1a54df28f9\",\"rankType\":1}"
headers = {
    'Content-Type': "application/json",
    'Cookie': "ticket = VFZSWlBRPT07SlNVakp5VW5KU1VqOzE2MTY="
    }
response = requests.request("POST", url, data=payload, headers=headers)
'''
url = "https://eduplan.leke.cn/auth/student/forecast/profession/getOptimizationCollegeOrMajor.htm"

payload = "{\"curPage\":1,\"objectId\":\"5ca2ce665db0dc1a54df28f9\",\"pageSize\":80,\"rankType\":1}"
headers = {
    'Content-Type': "application/json",
    'Cookie': "ticket = VFZSWlBRPT07SlNVakp5VW5KU1VqOzE2MTY="
    }
response = requests.request("POST", url, data=payload, headers=headers)
college_dict = json.loads(response.text)
#print(college_dict)
college_list = college_dict['data']['professionForecastOutDTOS']
for i in range(0,79):
	id = college_list[i]['id']
	collegeId = college_list[i]['collegeId']
	professionId = college_list[i]['professionId']
	proAliasName = college_list[i]['proAliasName']
	collegeName = college_list[i]['collegeName']

	url1 = "https://eduplan.leke.cn/auth/student/forecast/profession/addToCache.htm"
	payload = "{\"collegeId\":"+ str(collegeId) + ",\"collegeName\":\"" + str(collegeName) + "\",\"id\":" + str(id) + ",\"operateType\":1,\"proAliasName\":\"" + str(proAliasName) + "\",\"professionId\":" + str(professionId) +",\"key\":\"eduplan.volunteer.\"}"	
	headers = {
	    'Content-Type': "application/json",
	    'Cookie': "ticket = VFZSWlBRPT07SlNVakp5VW5KU1VqOzE2MTY="
	    }
	response = requests.request("POST", url1, data=payload.encode(), headers=headers)