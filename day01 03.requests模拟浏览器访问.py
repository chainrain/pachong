"""
用程序去获取网站数据时,
response.request.headers的'User-Agent'为'python-requests/2.20.1',
识别为python软件,爬取的网站数据就不完整,
如果要爬取完整的网站数据,就要伪装浏览器访问,
把User-Agent改为浏览器
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

response = requests.get('http://www.baidu.com',headers=headers)

print('响应体请求头',response.request.headers)
print('响应体',response.content.decode())