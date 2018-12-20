import importlib

# 目标: 根据类全名: 模块.类名, 创建该类对象

full_name = 'spiders.baidu_spider.BaiduSpider'

# 1. 获取模块名和类名
# rsplit, 从右往左截取
# rs = full_name.rsplit('.', maxsplit=1)
# print(rs)
module_name, class_name =  full_name.rsplit('.', maxsplit=1)
# 2. 使用动态导入模块, 根据模块名导入模块
module = importlib.import_module(module_name)
# 3. 使用getattr, 根据类名, 从模块中取出类
# getattr:
# 1. 获取模块中类; 第一个参数为模块, 第二参数是类名
# 2. 获取对象中属性: 第一个参数对象, 第二参数是属性名
cls = getattr(module, class_name)
# 4. 使用类创建, 创建实例对象
instance = cls()
print(instance)
print(instance.start_urls)


