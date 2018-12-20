# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Day08TencentItem(scrapy.Item):
    """定义字段: 在爬虫py里,输出的数据,只有定义的字段才能使用否则就报错"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()               # 职位名称
    category = scrapy.Field()           # 类别
    publish_time = scrapy.Field()       # 发布时间
    content = scrapy.Field()            # 工作职责(每一个职位的href里面得到的数据)