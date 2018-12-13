

import random
import requests

# 1. 准备代理IP列表
proxies_list = [
    {'http': 'http://114.43.54.194:80'},
    {'http': 'http://49.51.195.24:1080'},
    {'http': 'http://60.255.186.169:8888'},
    {'http': 'http://124.89.97.43:80'},
]

for i in range(10):
    proxies = random.choice(proxies_list)
    try:
        # 2. 随机取出一个代理IP


        # 3. 使用这个代理IP发送请求
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.content.decode())
    except Exception as ex:
        print(ex)
        proxies_list.remove(proxies)
print('proxies_list',proxies_list)
