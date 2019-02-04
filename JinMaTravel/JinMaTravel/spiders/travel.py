# -*- coding: utf-8 -*-
import scrapy
import requests
import re
"""
使用
(pachong) python@ubuntu:~/Desktop/pachong$ scrapy crawl travel -o ../../../../JinMa.csv
"""
from copy import deepcopy


class TravelSpider(scrapy.Spider):
    name = 'travel'
    allowed_domains = ['www.jinmalvyou.com']
    start_urls = ['http://www.jinmalvyou.com/']

    def parse(self, response):
        # 周边游
        small_categorys = response.xpath('//div[@class="leftNav topDesti"]/ul/li[1]/div/div/dl/dd/em')
        # 出境游
        small_categorys += response.xpath('//div[@class="leftNav topDesti"]/ul/li[2]/div/div/dl/dd/em')
        # 国内游
        small_categorys += response.xpath('//div[@class="leftNav topDesti"]/ul/li[3]/div/div/dl/dd/em')


        for small_category in small_categorys:
            item = {}
            item['小分类'] = small_category.xpath('./a/text()').extract_first()
            if str(small_category.xpath('./a/@href').extract_first().find('http')) == '1':
                item['小分类url'] = small_category.xpath('./a/@href').extract_first()
            else:
                item['小分类url'] = 'http:' + small_category.xpath('./a/@href').extract_first()
            # print(item)
            yield scrapy.Request(item['小分类url'], callback=self.parse_list, meta={'item': deepcopy(item)})

    def parse_list(self,response):
        item = response.meta['item']
        # print(response.url)
        travels = response.xpath('//ul[@class="rl-b2"]//li')
        # print(travels)

        # 下一页
        nexts = response.xpath('//div[@class="page"]/ul/div/a[@class="num"]/@href').extract()
        print(type(nexts))
        # print(nexts)
        for nex in nexts:
            print(nex)
            yield scrapy.Request('http://www.jinmalvyou.com' + nex, callback=self.parse)

        for travel in travels:
            item['旅游团名'] = travel.xpath('./div/div/p/a/text()').extract_first()
            item['旅游团介绍'] = travel.xpath('./div/div/p[2]/text()').extract_first()
            item['旅游团价格'] = travel.xpath('./div/div[3]/p/strong/text()').extract_first() + '元'
            item['旅游团网页'] = 'http://www.jinmalvyou.com' + travel.xpath('./div/div/p/a/@href').extract_first()

            print(item)
            yield item



