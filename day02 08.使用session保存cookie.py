"""
使用requests.session处理cookie
前面使用手动的方式使用cookie，那么有没有更好的方法在requets中处理cookie呢？

requests 提供了一个叫做session类，来实现客户端和服务端的会话保持

会话保持有两个内涵：

保存cookie，下一次请求会带上前一次的cookie
实现和服务端的长连接，加快请求速度

http://www.renren.com/SysHome.do
登录界面,里面from表单提交的地址是http://www.renren.com/PLogin.do
"""
import requests

# 获取session对象,把登录信息记录在cookie里
session = requests.session()
session.headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

# from表单提交的url
login_url = 'http://www.renren.com/PLogin.do'
# 登录参数
data = {
    'email':'18665625762',
    'password':'qq292605957'
}
response = session.post(login_url,data=data)

url = 'http://www.renren.com/901245995/profile'  # 我的主页

response_1 = session.get(url=url)

print(response_1.content.decode())