#coding:utf-8
import json
'''
删除swagger中pad和m的接口
'''
def del_swagger_m_hd():
	with open('D:/git/cnstrong/swagger.json','r', encoding='UTF-8') as f:
		#json转dict，取出paths下的各个接口的键	
		temp = json.load(f)
		json_paths = temp['paths']
		#print(type(temp))
		key_json = json_paths.keys()
		#print(list(key_json))
		#取出含有m和hd的键，并在字典中删除键值
		del_list = []
		for i in key_json:
			#print(i)
			if "/hd/" in i:
				del_list.append(i) 

			elif "/m/" in i:
				del_list.append(i)

		for j in del_list:
			del json_paths[str(j)]
		#print(json_paths)
		#替换paths的值返回
		temp.update(paths=json_paths)
		#lastjson = json.dumps(temp, ensure_ascii=False)
		return temp

with open("D:/git/cnstrong/test.json","w", encoding='UTF-8') as ff:
     json.dump(del_swagger_m_hd(),ff,ensure_ascii=False)