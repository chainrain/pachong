# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from day08_tencent.spiders.zhaopin3 import ZhaopinSpider


class Day08TencentPipeline(object):
    """管道用来数据存储和数据连接"""

    def open_spider(self, spider):
        """爬虫开启时候执行,只执行一次"""
        if isinstance(spider, ZhaopinSpider):  # 如果运行的是zhaopin3的ZhaopinSpider,就执行以下操作
            self.file = open('tencent_zhaoping.jsonlines', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, ZhaopinSpider):
            json.dump(dict(item), self.file, ensure_ascii=False)
            self.file.write('\n')
        return item

    def close_spider(self, spider):
        """爬虫结束时候执行,只执行一次"""
        if isinstance(spider, ZhaopinSpider):
            self.file.close()


"""
实现使用MongoDB来存储数据
1. 完善Pipeline的类
2. 在settings.py文件,开启该管道
"""
from pymongo import MongoClient


class TencentPipelineMongo(object):
    """实现使用MongoDB来存储数据"""
    def open_spider(self, spider):
        if isinstance(spider, ZhaopinSpider):
            self.client = MongoClient()
            self.collection = self.client['tencent']['zhaopin']

    def process_item(self, item, spider):
        """存储数据"""
        if isinstance(spider, ZhaopinSpider):
            # 需要把Item对象, 转换为字典
            self.collection.insert_one(dict(item))
            return item

    def close_spider(self, spider):
        if isinstance(spider, ZhaopinSpider):
            self.client.close()