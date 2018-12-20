"""
说明:
百度翻译windows版的,有做反扒系统,传参的时候有个token值,所以比较难爬
这里用到手机端的百度翻译,那里没有

准备检查当前语言类型的URL
http://fanyi.baidu.com/langdetect
准备翻译URL
http://fanyi.baidu.com/basetrans
数据:
query: hi(翻译内容)
from: en(内容语言)
to: zh(翻译成语言)
"""
import sys
import requests
import json

word = sys.argv[1]
# print(word)

# 翻译URL
basetrans_url = 'https://fanyi.baidu.com/basetrans'

# 检查当前语言类型的URL
detect_url = 'https://fanyi.baidu.com/langdetect'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
}

# 翻译数据
data = {'query': word}

# 获得要翻译的数据的语言
response = requests.post(url=detect_url,data=data,headers=headers)
print(response)
language = response.json()['lan']
# print(language)

# 翻译,组织data参数
data['from'] = language
# print(data)
if language == 'zh':
    data['to'] = 'en'
else:
    data['to'] = 'zh'
# data['to'] = 'en' if language == 'zh' else 'zh'  # 翻译成语言
# print(data)

response = requests.post(basetrans_url, data=data, headers=headers)
result = response.json()['trans'][0]['dst']
print(result)



