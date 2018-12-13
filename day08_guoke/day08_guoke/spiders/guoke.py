# -*- coding: utf-8 -*-
import urllib.parse

import scrapy


class GuokeSpider(scrapy.Spider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ask-list-cp']/li")
        # print('li_list',li_list)
        for li in li_list:
            # print('li',li)
            item = {}
            # 关注人数
            item['focus'] = li.xpath("./div/p/span/text()").extract_first()
            # 回答数
            item['answer'] = li.xpath("./div/p[2]/span/text()").extract_first()
            # url
            item['href'] = li.xpath("./div[2]/h2/a/@href").extract_first()
            # 标题
            item['title'] = li.xpath("./div[2]/h2/a/text()").extract_first()
            # 描述
            item['describe'] = li.xpath("./div[2]/p/text()").extract_first().strip()  # .strip()去除换行
            # 标签
            item['tag'] = li.xpath("./div[2]/div/p/a/text()").extract()
            # print('item',item)
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        """方法1"""
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse)

        """方法二"""
        # if next_url is not None:
        #     # next_url = urllib.parse.urljoin(response.url,next_url)
        #     print(next_url)
        #     # yield scrapy.Request(
        #     #     next_url,
        #     #     callback=self.parse  #用自己来提取下一页的数据
        #     # )
        #
        #
        #     # 使用response.follow方法，发送请求
        #     yield response.follow(
        #         next_url,  # 不完整的url地址，根据response的url拼接完整之后构造request对象
        #         callback=self.parse
        #     )