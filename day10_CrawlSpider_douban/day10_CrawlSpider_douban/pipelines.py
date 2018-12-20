# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
保存数据
1. 完善 DoubanPipeline 类
2. 在settings.py中开启
"""
from pymongo.mongo_client import MongoClient

from day10_CrawlSpider_douban.spiders.douban import DoubanSpider


class Day10CrawlspiderDoubanPipeline(object):
    def open_spider(self, spider):
        """连接mongo数据库"""
        if spider.name == DoubanSpider.name:
            self.client = MongoClient()
            self.collection = self.client['douban']['top250']

    def process_item(self, item, spider):
        """保存数据"""
        if spider.name == DoubanSpider.name:
            self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        """关闭连接数据库"""
        if spider.name == DoubanSpider.name:
            self.client.close()
