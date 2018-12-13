"""
re模块有个compile方法
用来提前准备正则表达式
"""



import re

regex = re.compile('\d')  # 正则方法

rs = regex.findall('chain1rain2')  # 搜索数字
print(rs)
rs = regex.sub('_','chain1rain2')  # 替换_
print(rs)

regex = re.compile('.+',re.S)  # 正则方法
rs = regex.findall('ab\nc')
print(rs)