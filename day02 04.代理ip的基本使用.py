"""
发送http的请求的时候,就使用http类型的代理, 如果没有就不使用代理了
发送https的请求的时候,就使用https类型的代理, 如果没有就不使用代理
"""

import requests

proxies = {
    'https':'https://89.22.175.42:8080',
    'http':'http://45.113.69.177:1080',
}
response = requests.get('https://httpbin.org/get',proxies=proxies)
print(response.content.decode())