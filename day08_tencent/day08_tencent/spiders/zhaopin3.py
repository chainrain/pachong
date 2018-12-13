# -*- coding: utf-8 -*-
import scrapy

from day08_tencent import items

"""
总结:......scrapy引擎还是快啊.......不过应该没有requests快吧....
实现从每一个职位的href里面得到工作职责的数据,组成整体
"""


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin3'
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
            # 职位的详情页面url
            detail_url = 'https://hr.tencent.com/' + tr.xpath('./td[1]/a/@href').extract_first()
            # print(item)
            # print('detail_url',detail_url)
            # 构建请求对象, 交给引擎
            # 把列表页中的数据, 传递给详情页, 通过meta的字典参数,callback循环parse_detail
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})

        # 实现翻页
        next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # 判断是否有下一页(没有下一页的特征为//*[@id="next"]/@href等于javascript:;)
        if next_url != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_url
            print(next_url)
            # 把请求交给scrapy引擎,callback循环parse
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        """从每一个职位的href里面得到工作职责的数据"""
        item = response.meta['item']
        # //*[@id="position_detail"]/div/table/tbody/tr[3]/td
        item['content'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[3]/td/ul/li/text()').extract())
        print(item)
        # 把请求交给scrapy引擎
        yield item