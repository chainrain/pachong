
# 首先导入所有的默认配置信息
from .default_settings import *

# 最后: 导入项目中配置信息, 后导入项目配置信息, 就会覆盖默认配置信息,报红没关系
from settings import *

# import sys
# print(sys.path)
# /Users/itheima/Documents/爬虫项目/day13/code/framework/project_dir
# /Users/itheima/Documents/爬虫项目/day13/code/framework
# 从这里我们可以看出, 框架首先会加载项目中的配置信息