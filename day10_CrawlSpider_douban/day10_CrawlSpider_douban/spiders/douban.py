# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
爬取: 'https://movie.douban.com/top250'
3. 创建CrawlSpider爬虫
4. 完善CrawlSpider爬虫
4.1 完善规则
4.2 完善提取函数
"""


from day10_CrawlSpider_douban.items import Day10CrawlspiderDoubanItem  # 要设置爬虫目录为源目录

class DoubanSpider(CrawlSpider):
    name = 'douban_top250'
    aallowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        # 因为豆瓣的第一页没有url,所以要把follow设为true,然后重复爬取,在其他网页找到第一页的url(follow会实现去重)
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url)
        # 获取包含电影信息的li标签列表
        lis = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # 遍历lis, 获取电影信息
        for li in lis:
            # 在item文件里定义允许输出的字段,如果没有的话,就报不允许的错误
            item = Day10CrawlspiderDoubanItem()
            item['movie_name'] = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['movie_desc'] = ''.join([i.strip() for i in  li.xpath('./div/div[2]/div[2]/p[1]//text()').extract()])
            item['movie_desc'] = item['movie_desc'].replace('\xa0', ' ')
            item['movie_intro'] = li.xpath('.//span[@class="inq"]/text()').extract_first()
            print(item)
            yield item
