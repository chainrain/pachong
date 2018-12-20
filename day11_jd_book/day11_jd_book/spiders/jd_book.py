# -*- coding: utf-8 -*-
import json

import scrapy
from copy import deepcopy

"""
需求：抓取京东图书的信息
目标：抓取京东图书信息包含: 图书所属大分类、图书所属小的分类、分类的url地址, 图书的名字、封面图片地址、图书url地址、作者、出版社、出版时间、价格

实现一个基于scrapy_reids的增量式爬虫
1. 实现一个普通scrapy爬虫
2. 修改为基于scrapy_reids的增量式爬虫; 只需要修改配置文件即可
"""


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['jd.com','3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        """1.2 提取大分类, 小分类信息"""
        # dts:大分类列表
        big_categorys = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')

        # 大分类详情
        for big_category in big_categorys:
            item = {}
            # 大分类名称
            item['big_category_name'] = big_category.xpath('./a/text()').extract_first()
            # 大分类URL
            item['big_category_url'] = response.urljoin(big_category.xpath('./a/@href').extract_first())
            # 小分类列表
            small_categorys = big_category.xpath('./following-sibling::dd[1]/em')
            for small_category in small_categorys:
                # 小分类的名字
                item['small_category_name'] = small_category.xpath('./a/text()').extract_first()
                # 小分类的URL
                item['small_category_url'] = response.urljoin(small_category.xpath('./a/@href').extract_first())  # 因为URL没有前缀,所以要加上response.urljoin
                yield scrapy.Request(item['small_category_url'],callback=self.parse_book_list,meta={'item':deepcopy(item)})


    def parse_book_list(self,response):
        """请求小分类的URL,解析数据"""
        item = response.meta['item']
        # 所有图书
        books = response.xpath('//div[contains(@class, "j-sku-item")]')
        # 遍历
        for book in books:
            # 图书名字,有空格strip()去除
            item['book_name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            # 图书封面图片,图片有两种名src和data-lazy-img,所以要加判断
            item['book_img'] = book.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            if item['book_img'] is None:
                item['book_img'] = book.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img').extract_first()
            item['book_img'] = response.urljoin(item['book_img'])  # 因为URL没有前缀,所以要加上response.urljoin
            # 图书url地址
            item['book_url'] = response.urljoin(book.xpath('.//div[@class="p-name"]/a/@href').extract_first())
            # 作者
            item['book_author'] = ' '.join(book.xpath('.//span[@class="p-bi-name"]/span/a/text()').extract())
            # 出版社
            item['book_publisher'] = book.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first()
            # 出版时间,有空格strip()去除
            item['book_publish_time'] = book.xpath('.//span[@class="p-bi-date"]/text()').extract_first().strip()
            # 价格发现是动态生成出来的,所以直接定位是找不到的,后来在:请求页面,开发者工具,三点,search,随便找一个价格,点击函数,右键函数名,点击copy link address ,打开网址,发现第一个op就是价格,而j_xx就是这个商品的id,url的j_xx,和页面的data-sku一样,那么就用这个data-sku的值,发起请求,得到商品的价格
            price_url = 'https://p.3.cn/prices/mgets?skuIds=J_{}'
            skuIds = book.xpath('./@data-sku').extract_first()
            price_url = price_url.format(skuIds)
            yield scrapy.Request(price_url,callback=self.parse_book_price,meta={'item':deepcopy(item)})
        # 分页
        # 获取下一页URL
        next_url = response.xpath('//a[@class="pn-next"]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)  # 补全URL
            # 构建下一页请求,回调获取书本详情函数
            yield scrapy.Request(next_url, callback=self.parse_book_list, meta={'item': deepcopy(item)})


    def parse_book_price(self,response):
        """解析价格"""
        item = response.meta['item']
        item['book_price'] = json.loads(response.text)[0]['op']
        print(item)
        # 把数据交给引擎
        yield item