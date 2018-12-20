"""
### 9. 实现框架多管道
- `目标`: 实现框架支持多管道,每个管道清理不同数据
- `步骤`:
   - 在项目文件夹下:
      - 创建pipelines.py文件
      - 定义DoubanPipeline和BaiduPipeline管道类
      - 修改mian.py, 准备管道列表, 传递给引擎
"""
from spiders.baidu_spider import BaiduSpider
from spiders.douban_spider import DoubanSpider


class BaiduPipeline(object):
    def process_item(self, item, spider):
        if spider.spider_name == BaiduSpider.spider_name:
            print("百度管道数据: {}".format(item.data))

        return item


class DoubanPipeline(object):
    def process_item(self, item, spider):
        if spider.spider_name == DoubanSpider.spider_name:
            print("豆瓣管道数据: {}".format(item.data))
        return item
