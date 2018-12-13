"""
说明:
http://httpbin.org 是一个专门用于测试http请求网站
requests.post(url, data={}, headers={}) # POST请求
这个网站没有做反扒系统,所以不用模拟浏览器
"""

import requests

url = 'http://httpbin.org/post'

data = {
    'name':'chainrain'
}

response = requests.post(url=url,data=data)

print(response.content.decode())