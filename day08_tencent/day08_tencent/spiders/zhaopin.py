# -*- coding: utf-8 -*-
import scrapy

from day08_tencent import items

"""
(单页版)
实现从页面提取岗位信息, 职位类别 和 发布时间
"""

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 提取所有岗位信息, 职位类别 和 发布时间
        # 用浏览器定位的是//*[@id="position"]/div[1]/table/tbody/tr,但是response响应中没有tbody
        # xpath 要以响应内容为准, 所以去掉tbody
        trs = response.xpath('//*[@id="position"]/div[1]/table/tr')[1:-1]
        # print(trs)('./td[last()]/text()').extract_first()
        for tr in trs:
            item = items.Day08TencentItem()
            # 职位名字
            item['name'] = tr.xpath('./td[1]/a/text()').extract_first()
            # 类别
            item['category'] = tr.xpath('./td[2]/text()').extract_first()
            # 发布时间
            item['publish_time'] = tr.xpath('./td[last()]/text()').extract_first()
            print(item)
            yield item