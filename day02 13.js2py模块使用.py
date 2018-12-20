"""
js2py模块
安装 pip3 install js2py
"""

import js2py

# 创建js执行环境
context = js2py.EvalJs()

# 添加变量,注意不能多层赋值,context.c.d = 100
context.a = 10
context.b = 20
print(context.a)

# 添加函数
js = '''
function sum(a ,b){return a+b;}
rs = sum(a,b);
'''

# 执行js环境
context.execute(js)

# js环境的rs
print(context.rs)

# 第二种方法,直接添加值
rs = context.sum(100,200)
print(rs)

context.c = {'d': 100}
print(context.c)
print(type(context.c))  # 不是字典,是js2py.base.JsObjectWrapper
print(type(context.c.to_dict()))