"""
获取所有城市名称
"""
import requests
import json
from jsonpath import jsonpath

# 发送请求, 获取城市的json格式字符串
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = requests.get(url=url)
# print(response.content.decode())

data = json.loads(response.content.decode())
# print(data)

citys = jsonpath(data,'$..name')
print(citys)