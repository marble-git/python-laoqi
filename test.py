
#coding=utf-8

'''
    This is my first python program.
    I will be a great programmer.
'''
#思路是最重要的


#导入框架 库，模块 pip install xxxxxxxx
import requests
import json
import time
import random
import hashlib

#1. 确定网址
url =  'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

#2.2 设置好请求体
data = {
'i': '新年好',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '16142844782582',
'sign': 'a287c91333e6a5eae8c24381f9830b04',
'lts': '1614284478258',
'bv': 'bc60a5ab7ddb6f48e25bb9e4fa514e20',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME'
}

"""

'salt': '16142844782582',
'sign': 'a287c91333e6a5eae8c24381f9830b04',
'lts': '1614284478258',

"""
#2.3 反爬 1.ua 2.cookie 3.referer

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',

'Cookie': 'OUTFOX_SEARCH_USER_ID=2018806040@10.108.160.208; JSESSIONID=aaaH-TsVBlSId7co1efEx; OUTFOX_SEARCH_USER_ID_NCOO=29640697.350261692; ___rl__test__cookies=1614284478255',

'Referer': 'http://fanyi.youdao.com/'
        }





#2. 请求 requests get拿数据  post(有请求体)发数据

result = requests.post(url,data=data,headers=headers).text

print(result)



#3.筛选数据

#dict_result = json.loads(result)
#print(dict_result)

#print(dict_result)["translateResult"



