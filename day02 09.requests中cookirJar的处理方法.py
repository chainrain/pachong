import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 请求百度
response = requests.get('http://www.baidu.com', headers=headers)
# 获取响应中cookie信息
print(type(response.cookies))  # RequestsCookieJa类型
print('response.cookies',response.cookies)

cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
print('cookie_dict',cookie_dict)