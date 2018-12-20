import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
# 超时参数: timeout, 用于指定一个超时时间, 单位是s
# 如果在指定秒数内返回, 正常
# 如果响应超过指定的秒数, 报超时错误 timeout=xx
response = requests.get('http://www.google.com', headers=headers,timeout=2)

print(response.content.decode())