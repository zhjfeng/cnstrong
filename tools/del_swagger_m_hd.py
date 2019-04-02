#coding:utf-8
import json
import requests
'''
删除swagger中pad和m的接口
'''
def get_swagger():
	url = "http://eduplan.leke.cn/v2/api-docs"
	response = requests.request("GET", url) 
	return json.loads(response.text)

def del_swagger_m_hd_py():
	temp = get_swagger()
	paths_new = {k:v for k,v in temp['paths'].items() if '/hd/' not in k and '/m/' not in k}
	temp.update(paths=paths_new)
	return temp

with open("E:/git/cnstrong/test.json","w", encoding='UTF-8') as ff:
	json.dump(del_swagger_m_hd_py(),ff,ensure_ascii=False)

#java式
def del_swagger_m_hd_java():
	temp = get_swagger()
	json_paths = temp['paths']
	key_json = json_paths.keys()
	#取出含有m和hd的键，并在字典中删除键值
	del_list = []
	for i in key_json:
		if "/hd/" in i:
			del_list.append(i) 

		elif "/m/" in i:
			del_list.append(i)

	for j in del_list:
		del json_paths[str(j)]
	#替换paths的值返回
	temp.update(paths=json_paths)
	#lastjson = json.dumps(temp, ensure_ascii=False)
	return temp