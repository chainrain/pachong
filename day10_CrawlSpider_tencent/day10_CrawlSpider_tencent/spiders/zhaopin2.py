# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zhaopin2Spider(CrawlSpider):
    name = 'zhaopin2'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 翻页的所有页面
        Rule(LinkExtractor(allow=r'position.php\?&start=\d+'), follow=True),

        # 每个职位的详情页
        Rule(LinkExtractor(allow=r'position_detail.php'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        """提起详情页的数据(职位Rule里面有callback,所以会解析)"""
        item = {}
        item['职位'] = response.xpath('//*[@id="sharetitle"]/text()').extract_first()
        item['工作地点'] = response.xpath('//*[@id="position_detail"]/div/table/tr[2]/td[1]/text()').extract_first()  # 响应的页面是没有tbody的,所以不用加
        item['职位类别'] = response.xpath('//*[@id="position_detail"]/div/table/tr[2]/td[2]/text()').extract_first()  # 响应的页面是没有tbody的,所以不用加
        item['招聘人数'] = response.xpath('//*[@id="position_detail"]/div/table/tr[2]/td[3]/text()').extract_first()  # 响应的页面是没有tbody的,所以不用加
        item['工作职责'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[3]/td/ul/li/text()').extract())
        item['工作要求'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[4]/td/ul/li/text()').extract())
        print(item)
        yield item
