# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Day08ItcastPipeline(object):
    def process_item(self, item, spider):
        # 爬虫文件中提取数据的方法每yield一次item，就会运行一次
        # 该方法为固定名称函数
        print(item)
        return item
