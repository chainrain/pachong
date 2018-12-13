# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zhaopin3Spider(CrawlSpider):
    name = 'zhaopin3'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 翻页的所有页面
        Rule(LinkExtractor(allow='position.php\?&start=\d+#a'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response.url)
        i = {}

        # 不同规则直接无法进行数据传递, 但是在解析函数中可以构建请求, 传递数据的.
        yield scrapy.Request('detail_url', callback='parse_detail', meta={})