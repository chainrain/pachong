# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        """http://book.dangdang.com/的解析"""
        divs = response.xpath('//div[@class="level_one "]')[2:-4]  # 注意,1:这里拿的是源码,所以源码的level_one的后面有个空格,这个空格elements里面是没有的.2:因为源码里拿到其他的level_one,所以就要切割
        # print(divs)
        print(len(divs))
        for div in divs:
            item = {}
            # 注意: 响应中没有span标签, 有大分类中没有a标签
            item['大标签名'] = ''.join([i.strip() for i in div.xpath('./dl/dt//text()').extract()])
            a_s = div.xpath('.//dl[@class="inner_dl"]/dd/a')
            for a in a_s:
                item['小标签名'] = a.xpath('./text()').extract_first()
                item['小标签的URL'] = a.xpath('./@href').extract_first()
                # print(item)
                yield scrapy.Request(item['小标签的URL'],callback=self.parse_book_list,meta={'item':deepcopy(item)})


    def parse_book_list(self,response):
        """小分类URL的解析"""
        item = response.meta['item']
        books_list = response.xpath('//ul[contains(@id, "component")]/li')

        for books in books_list:
            item['图书名字'] = books.xpath('./p[@class="name"]/a/text()').extract_first()
            item['图书封面'] = books.xpath('./a/img/@data-original').extract_first()
            if item['图书封面'] is None:
                item['图书封面'] = books.xpath('./a/img/@src').extract_first()
            item['图书URL'] = books.xpath('./p[@class="name"]/a/@href').extract_first()
            item['图书作者'] = ''.join(books.xpath('./p[@class="search_book_author"]/span[1]//text()').extract())
            item['出版社'] = books.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            item['出版时间'] = books.xpath('./p[@class="search_book_author"]/span[2]/text()').extract_first()
            item['图书价格'] = books.xpath('.//span[@class="search_now_price"]/text()').extract_first()
            print(item)

        # 获取下一页的URL
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        # 如果有下一页, 把URL进行补全, 构建请求请求, 交给引擎
        if next_url:
            next_url = response.urljoin(next_url)
            print(next_url)
            # 构建请求请求, 交给引擎
            yield scrapy.Request(next_url, callback=self.parse_book_list, meta={'item': deepcopy(item)})
