# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Day10CrawlspiderDoubanItem(scrapy.Item):
    """如果再爬虫里用了这个类来定义item,就要在这里允许,不然会报错:Day10CrawlspiderDoubanItem does not support field: 电影名称"""
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    movie_score = scrapy.Field()
    # 描述信息
    movie_desc = scrapy.Field()
    # 简介
    movie_intro = scrapy.Field()
