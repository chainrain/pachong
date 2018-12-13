import requests
import js2py

# 准备获取rkey
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
}

rkey = 'http://activity.renren.com/livecell/rKey'
response = requests.get(url=rkey, headers=headers)
# {'data': {'msg': 'ok', 'maxdigits': '19', 'code': 0, 'isEncrypt': True, 'n': '91eb08c0d76c37fc1d7521fbaabbeef5d1d88063e7bb2ef24b9a08f0347ec617', 'rkey': 'fa647ac3744264c8eece684183c36fe5', 'e': '10001'}}
# print(response.json())  # 目的是去到data的头
# {'msg': 'ok', 'maxdigits': '19', 'code': 0, 'isEncrypt': True, 'n': '91eb08c0d76c37fc1d7521fbaabbeef5d1d88063e7bb2ef24b9a08f0347ec617', 'rkey': 'fa647ac3744264c8eece684183c36fe5', 'e': '10001'}
n = response.json()['data']
# print(n)



# 创建js环境
context = js2py.EvalJs()
# 准备参数
context.t = {
    'password': 'qq292605957'
}
context.n = n


# 准备js执行环境
def get_js_from_url(url):
    response = requests.get(url=url, headers=headers)
    return response.content.decode()


# 把需要加载的js全部加载进来,如果这里不知道要加载哪几个个js,那就把所有js都加载进来
context.execute(get_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'))
context.execute(get_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'))
context.execute(get_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'))
context.execute(get_js_from_url('http://s.xnimg.cn/a86836/wap/mobile/wechatLive/js/celllog.js'))
# 加载函数
js = '''
t.password =t.password.split("").reverse().join(""),
            setMaxDigits(130);
            var o = new RSAKeyPair(n.e,"",n.n)
            , r = encryptedString(o, t.password);
'''
context.execute(js)
# print(context.r)  # 拿到执行完js的r
password = context.r

# 登录url
login_url = 'http://activity.renren.com/livecell/ajax/clog'

# 登录url需要发送的参数,登录url下面有个from data可以看到
data = {
    'phoneNum': '18665625762',
    'password': password,
    'c1': -100,
    'rKey': n['rkey']
}

# 登录
response = requests.post(url=login_url, data=data, headers=headers)
print(response.content.decode())
