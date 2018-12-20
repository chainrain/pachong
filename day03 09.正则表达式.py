import re


index = re.findall('a','abca')  # 搜索有几个a

index = re.findall('.','abc\nabc')  # .搜索任意字符(除了\n)

index = re.findall('.','abc\nabc',re.S)  # .搜索任意字符(包括\n)
index = re.findall('.','abc\nabc',re.DOTALL)  # .搜索任意字符(包括\n)

index = re.findall('\.','12.36')  # \.搜索源生点

index = re.findall('\d', '123abc')  # 数字
index = re.findall('\D', '123abc')  # 非数字


index = re.findall('\s', '123 a\tb\rc\nd')  # \s: 空白符: 包含空格,\t,\r,\n
index = re.findall('\S', '123 a\tb\rc\nd')  # .搜索任意字符(除了\t,\r,\n转义符号)

index = re.findall('\w', '12ab呵呵_%$$#$')  # \w: 用于字母, 数字, _, 中文
index = re.findall('\W', '12ab呵呵_%$$#$')  # \W: 用于符号

index = re.findall('.*', 'abc\nab')  # .*搜索0或者多次
index = re.findall('.+', 'abc\nab')  # .*搜索1或者多次
index = re.findall('.?', 'abc\nabb')  # ?: 0 或 1次
index = re.findall('.{3}', 'abc\nab')  # 任意字符3个
index = re.findall('.{2,3}', 'abcd\nab')  # 任意字符最多2个到3个
index = re.findall('.{2,}', 'abcd\n2b')  # 任意字符2个以上
print(index)


sub = re.sub('\d+','_','chain1rain')  # 将数字替换成_
print(sub)


chinese = re.findall('[\u4e00-\u9fa5]+',"你好,hello.世界,world")  # 只留下中文
print(chinese)

# r原串在字符串中使用: 常见使用场景就是: windows路径
print(len('\n'))
print(len(r'\n'))
print(len('\\n'))

print('a\nb' == 'a\nb')  # True
print(r'a\nb' == 'a\nb')  # False
print(r'a\nb' == 'a\\nb')  # True

rs = re.findall('a\nb', 'a\nb') #['a\nb']
rs = re.findall(r'a\nb', 'a\nb') #['a\nb']
rs = re.findall('a\\nb', 'a\\nb') #[]
rs = re.findall('a\\\\nb', 'a\\nb') #['a\\nb']
rs = re.findall(r'a\\nb', 'a\\nb') #['a\\nb']
print(rs)


"""
总结: 如果正则中没有小括号, 使用整个正则表达式作为要提取数据
      如果有小括号, 它只会提取和小括号匹配内容, 小括号两边是用于定位数据的
"""
rs = re.findall(r"a.+bc", "a\nbc", re.DOTALL)
print(rs) # a\nbc
rs = re.findall(r"a(.+)bc", "a\nbc", re.DOTALL)
print(rs) # ['\n']
rs = re.findall(r"a(.+)b(.+)c", "a\nb\nc", re.DOTALL)
print(rs) # [('\n', '\n')]




"""
贪婪: 就是尽可能多的匹配内容, *, + 默认都贪婪的
非贪婪: 就是尽可能少的匹配内容 *?, +?
"""
string_a = '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t\t<meta http-equiv="content-type" content="text/test;charset=utf-8">\n\t\t<meta content="always" name="referrer">\n        <meta name="theme-color" content="#2932e1">'
ret = re.findall("<.*>", string_a, re.S)  # 直到最后一个>符号的时候,为一个数值,所有只有一个整体
print(ret)
print(len(ret)) # 1

ret = re.findall("<.*?>", string_a, re.S)  # 到第一个>符号的时候,就为一个数值,所有有4个
print(ret)
print(len(ret))  # 4
