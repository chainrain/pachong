# -*- coding: utf-8 -*-
import scrapy

from day08_tencent import items

"""
页面找到下一个翻页的url,实现翻页
"""

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin2'
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

        # 实现翻页
        next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # 判断是否有下一页(没有下一页的特征为//*[@id="next"]/@href等于javascript:;)
        if next_url != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_url
            print(next_url)
            # 把请求交给scrapy引擎
            yield scrapy.Request(next_url, callback=self.parse)
