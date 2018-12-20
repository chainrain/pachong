# -*- coding: utf-8 -*-
import json
import re

import scrapy
from copy import deepcopy
import requests


class TravelSpider(scrapy.Spider):
    name = 'travel'
    global place
    place = 'all'

    allowed_domains = ['www.gzl.com.cn']
    # start_urls = ['http://www.gzl.com.cn/search/all/xianggelila.html']
    start_urls = ['http://www.gzl.com.cn/search/all/{}.html'.format(place)]
    # start_urls = ['http://www.gzl.com.cn/search/all/guangzhou.html']

    def parse(self, response):
        global place
        all_travel = response.xpath('//ul[@class="prod-list"]/li')
        # print(all_travel)
        # print(len(all_travel))
        for travel in all_travel:
            item = {}
            item['团名称'] = travel.xpath('./a/div/div/text()').extract_first()
            item['简介'] = travel.xpath('./a/div/div[3]/p/span/text()').extract_first()
            day = travel.xpath('./a/div/div[3]/div[2]/text()').extract_first()
            item['天数'] = re.findall('.天', day)
            item['旅行人数'] = travel.xpath('./a/div/div[3]/div[5]/div[1]/span/text()').extract_first()
            item['价格'] = travel.xpath('./a/div/div[3]/div[4]/text()').extract_first() + '￥'  # 这个只是主页的价格,并不是页面内的价格
            item['网址'] = travel.xpath('./a/@href').extract_first()
            print(len(item))
            # print(item)
            yield scrapy.Request(item['网址'], callback=self.parse_detail, meta={'item': deepcopy(item)})
        # 翻页模板,第一页已经拿到,要拿其他

        # next_url = response.xpath('//div[@class = "pagination"]').extract()
        # next_url = response.xpath('//@showData').extract()
        # print(next_url)
        # yield

        page = response.body
        # print(type(page.decode()))
        # print(page.decode())
        page_total = re.findall('showData: (\d*)', page.decode())
        # print('page_total',page_total)
        total = re.findall("var total = '(\d*)", page.decode())
        # print('total',total)
        page = (int(total[0]) / int(page_total[0]))
        # print(page)
        # print(page // 1)
        if page // 1 != page:
            page = page//1 + 1
        # print('page',int(page))
        next_urls = int(page)
        for i in range(2,next_urls+1):
            # print(i)
            next_url = 'http://www.gzl.com.cn/search/all/{}.html?page={}'.format(place,i)
            print('next_url',next_url)
            yield scrapy.Request(next_url,callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        # print(response.url)
        # prices = response.xpath('//div[@class="prod-pri-item"]/span/em').extract_first()
        # print(prices)
        pdid = re.findall('domestic/(.*?).html', response.url)
        # print(pdid)
        url = 'http://www.gzl.com.cn/grouptour/scheduleDateMap.json'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        data = {'pdId': pdid}

        index = requests.post(url=url, data=data, headers=headers)
        prices = index.content.decode()
        # print(type(prices))
        dict_prices = json.loads(prices)
        dict_prices = dict_prices['ScheduleDateMap']
        # print(dict_prices)
        # print(type(dict_prices))
        item['详细价格'] = dict_prices
        # print(item)
        yield item
