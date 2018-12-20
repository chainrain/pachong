import json

json_str = '{"name":"老王", "age":18, "gender":"男", "hobby":["练腰", "运动"]}'
print(json_str)
print(type(json_str))

json_dict = json.loads(json_str)
print(json_dict)
print(type(json_dict))

json_new = json.dumps(json_dict,ensure_ascii=False)
print(json_new)
print(type(json_new))

json_new1 = json.dumps(json_dict,ensure_ascii=False,indent=2)
print(json_new1)
print(type(json_new1))


# json文件对象 和 python数据转换
# 把python类型数据, 以json格式写入到文件中: dump
#  ensure_ascii=False 有的操作系统会报错,此时就需要encoding='utf-8'
with open('01_test.json','w',encoding='utf-8') as f:
    json.dump(json_dict,f,ensure_ascii=False,indent=4)


# 把json文件中数据 转换为 python类型的数据: load
#  有的操作系统会报错,此时就需要encoding='utf-8'
with open('01_test.json','r',encoding='utf-8') as f:
    new_dict = json.load(f)
    print(new_dict)