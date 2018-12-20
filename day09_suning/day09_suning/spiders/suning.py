# -*- coding: utf-8 -*-
import re

import scrapy
from copy import deepcopy

"""
爬取苏宁图书
"""

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        """解析页面,获取主分类,小分类"""
        # 一级菜单(主分类)
        divs = response.xpath('//div[@class="menu-item"]')  # 定位所有class 为 menu-item的div
        # 二级菜单(小分类)
        sub_divs = response.xpath('//div[contains(@class, "menu-sub")]')  # 定位所有class 包含 menu-sub的div
        # print(divs)
        # print(sub_divs)

        for div in divs:
            """
            遍历divs, 获取主分类小分类信息
            """
            item = {}
            item['主分类'] = div.xpath('./dl/dt/h3/a/text()').extract_first()
            item['主分类URL'] = div.xpath('./dl/dt/h3/a/@href').extract_first()

            a_s = div.xpath('./dl/dd/a')
            # a_s = div.xpath('./dl/dd/a/text()').extract()  # 校验数据a_s
            # print('a_s',a_s)  # 进口原版书,期刊杂志,音像的a_s为空(小类别)

            if len(a_s) == 0:
                """
                进口原版书,期刊杂志,音像的没有小分类,
                再从弹出层的子菜单中, 小分类的a标签列表
                """
                sub_div = sub_divs[divs.index(div)]
                a_s = sub_div.xpath('./div[1]/ul/li/a')
                # print(a_s)

            for a in a_s:
                """
                遍历大分类,得到小分类
                """
                item['小分类'] = a.xpath('./text()').extract_first()
                item['小分类URL'] = a.xpath('./@href').extract_first()
                # print(item)
                # yield item
                yield scrapy.Request(item['小分类URL'],callback=self.parse_book_list_url,meta={'item':deepcopy(item)})

    def parse_book_list_url(self,response):
        """解析每个小分类的书的url"""
        item = response.meta['item']
        print(item)
        print(response.url)
        print(response)
        ci = re.findall('1-(\d+?)-0',response.url)
        """"""
        # print('ci',ci)
        if len(ci) != 0:
            """
            得到分类的id(会有个别特殊的),例如:
            https://list.suning.com/1-264003-0.html 的 264003.这种的一页显示60条,一次刷新30条,分两次刷新,part_num = 2
            https://search.suning.com/%E6%AD%A6%E4%BE%A0/ 这种的话,正则就为空.走else,这种的一页显示60条,一次刷新30条,分两次刷新,part_num = 2
            """
            ci = ci[0]
            url_pattern = 'https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&paging={}'
            part_num = 2
        else:
            ci = re.findall('https://search.suning.com/(.+?)/', response.url)[0]
            url_pattern = 'https://search.suning.com/emall/searchV1Product.do?keyword={}&ci=0&pg=01&cp={}&paging={}'
            part_num = 4
        # 提取总页数
        pageNumbers = int(re.findall('param.pageNumbers\s*=\s*"(\d+)"',response.text)[0])
        # print('pageNumbers',pageNumbers)
        # print(ci)
        # print(url_pattern)

        for cp in range(0, pageNumbers):
            # cp 表示每一个页号
            for paging in range(0, part_num):
                # paging: 表示第几部分
                # ci:表示搜索的分类
                url = url_pattern.format(ci, cp, paging)
                # print(url)
                yield scrapy.Request(url, callback=self.parse_book_list, meta={'item': deepcopy(item)})

    def parse_book_list(self, response):
        """解析列表页"""
        # print(response.url)
        item = response.meta['item']
        # 获取包含图书信息的li标签列表
        # print(response.url)
        lis = response.xpath('//li[@ishwg]')
        # print(len(lis))
        # print(lis)
        for li in lis:
            # 图书名称
            item['书名'] = li.xpath('.//a[contains(@name, "pro_name")]/text()').extract_first()
            # 图书封面图片
            item['图书图片'] = li.xpath('.//img/@src').extract_first()
            if item['图书图片'] is None:
                item['图书图片'] = li.xpath('.//img/@src2').extract_first()
            item['图书图片'] = 'https:' + item['图书图片']
            # print(item)
            # 1.准备详情URL
            detail_url = 'https:' + li.xpath('.//a[contains(@name, "pro_name")]/@href').extract_first()
            # print(detail_url)
            # 2. 构建详情页请求
            yield scrapy.Request(detail_url, callback=self.parse_book_detail, meta={'item': deepcopy(item)})

    def parse_book_detail(self, response):
        """解析详情页"""
        item = response.meta['item']
        # 记录详情页URL
        item['书本详情URL'] = response.url
        # 出版商
        item['出版社'] = response.xpath('//*[@id="productName"]/a/text()').extract_first()
        # 生成价格URL

        # 1. 从详情页的URL中, 取出价格需要的数据
        datas = re.findall('https://product.suning.com/(\d+)/(\d+).html', response.url)[0]
        # 取出商品ID, 如果不足11位, 补齐11,前面补0
        pro_id = datas[1]
        while len(pro_id) < 11:
            pro_id = '0' + pro_id

        # 2. 生成价格的URL
        url_pattern = 'https://pas.suning.com/nspcsale_0_0000000{}_0000000{}_{}_10_010_0100101.html'
        price_url = url_pattern.format(pro_id, pro_id, datas[0])
        # print(price_url)
        # 3. 构建价格请求
        yield scrapy.Request(price_url, callback=self.parse_price, meta={'item': item})

    def parse_price(self, response):
        """解析价格信息"""
        item = response.meta['item']
        price = re.findall('"promotionPrice":"(\d+.\d+)"', response.text)
        # 如果没有促销价格, 获取网络价格
        if len(price) == 0:
            price = re.findall('"netPrice":"(\d+.\d+)"', response.text)
        item['图书价格'] = price[0]

        # print(item)
        # 把数据交给引擎
        yield item
