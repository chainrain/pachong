import requests

response = requests.get('http://www.baidu.com')
print('返回状态信息',response)
print('返回状态码',response.status_code)
print('响应头',response.headers)
print('响应对应的请求头',response.request.headers)
print('响应体(content得出)',response.content.decode())  # 默认为utf8解码.个别网站使用gbk编码,例如http://www.people.com.cn/,这些网站就要用gbk解码,response.content.decode('gbk')
response.encoding = 'utf-8'
print('响应体(text得出)',response.text)
print('响应的cookies',response.cookies)
# print('响应对应的请求头',response.request.hraders)  # 或者没有
