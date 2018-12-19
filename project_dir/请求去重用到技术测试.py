from w3lib.url import canonicalize_url
import hashlib

# 1. URL规范化处理: 就是对请求(?)后面参数进行排序
url1 =  'http://www.baidu.com?name=laowang&age=18'
url2 =  'http://www.baidu.com?age=18&name=laowang'
url1 = canonicalize_url(url1)
url2 = canonicalize_url(url2)
print(url1)
print(url2)

# 2. 对字典进行排序
params1 = {'name':'laowang', "age": 18}
params2 = {"age": 18, 'name':'laowang'}
# print(params1)
# print(params2)
print(params1.items())
# [('name', 'laowang'), ('age', 18)])

# 字典转换为元祖列表进行排序(字典排序)
params1 = sorted(params1.items(), key=lambda x:x[0])
params2 = sorted(params2.items(), key=lambda x:x[0])
print(params1)
print(params2)

# 3. 把字符串生成一个指纹
# 获取sha1算法对象
sha1 = hashlib.sha1()
# 向sha1算法中,添加原始数据
sha1.update(url1.encode())
# 获取16进制指纹字符串
fp = sha1.hexdigest()
print(fp)

# python3中; str是字符串, bytes二进制数据; 默认编码是utf-8; 编码encode, 解码decode
# python2中; str是二进制数据, unicode是字符串, 默认编码ascii;编码encode, 解码decode
# 写一个方法, 把字符串转为二进制, 无论是py2还是py3都可以
import six
def str_to_bytes(s):
    if six.PY3:
        # 如果是py3
        return s.encode('utf-8') if isinstance(s, str) else  s
    else:
        # 不是py3, 就是py2
        return s if isinstance(s, str) else s.encode('utf-8')


print(str_to_bytes('呵呵'))

