"""
json中的字符串都是双引号引起来的
如果不是双引号
eval：能实现简单的字符串和python类型的转化
replace：把单引号替换为双引号
往一个文件中写入多个json串，不再是一个json串，不能直接读取

一行写一个json串，按照行来读取 f.readline()
"""

import json

json_str = "{'name':'老王', 'age':18, 'gender':'男', 'hobby':['练腰', '运动']}"

# json_dict = json.loads(json_str)
# print(json_dict)

# 方案一
json_dict = json.dumps(json_str)
print(json_dict)
new_json = json.loads(json_dict)
print(new_json)

# 方案2: 把单引号替换为双引号(推荐)
json_str = json_str.replace("'",'"')
json_dict = json.loads(json_str)
print(json_dict)

# 方案: eval, 可以转换简单json格式字符串, 不支持bool类型的数据
dic2 = eval(json_str)
print(dic2)