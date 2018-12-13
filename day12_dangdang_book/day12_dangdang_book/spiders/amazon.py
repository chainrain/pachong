# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
亚马逊图书爬取
"""

class AmazonSpider(CrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051']

    rules = (
        # 提取所有图书分类的URL, 无需提取数据, 可以没有callback, 由于要提取新的URL所以follow要指定为True
        Rule(LinkExtractor(restrict_xpaths='//*[@id="leftNav"]/ul[1]/ul/div/li'),follow=True),
        # 提取图书列表页的URL,一共多少页. 无需提取数据, 可以没有callback, 由于要提取新的分页URL所以follow要指定为True
        Rule(LinkExtractor(restrict_xpaths='//*[@id="pagn"]'),follow=True),
        # 提取详情页URL, 需要从详情页提取数据, 需要指定callback, 无需从详情页提取URL, 所以follow为False
        Rule(LinkExtractor(restrict_xpaths='//a[contains(@class, "s-access-detail-page")]'),callback='parse_item',follow=False)

    )

    def parse_item(self, response):
        """详情页URL"""
        item = {}
        item['图书名'] = response.xpath('//*[contains(@id, "roductTitle")]/text()').extract_first()
        item['图书封面'] = response.xpath('//*[contains(@id, "mgBlkFront")]/@src').extract_first()
        item['图书URL'] = response.url
        item['图书作者'] = ''.join([i.strip() for i in response.xpath('//*[@id="bylineInfo"]//text()').extract()])  # 因为有可能又作者和译者,所以extract得到所有,再遍历去空格
        publishes = re.findall('<li><b>出版社:</b>\s*(.+?);.*?\((.+?)\)</li>', response.text)
        if len(publishes) != 0:
            item['出版社'] = publishes[0][0]
            item['出版时间'] = publishes[0][1]
        item['价格'] = response.xpath('.//span[contains(@class, "a-color-price")]/text()').extract_first()
        # 获取分类信息a标签列表
        a_s = response.xpath('//span[@class="a-list-item"]/a[text()]')
        # 图书所属大分类
        if len(a_s) > 0:
            item['大分类名'] = a_s[0].xpath('./text()').extract_first().strip()
            item['大分类URL'] = response.urljoin(a_s[0].xpath('./@href').extract_first())
        # 图书所属中的分类
        if len(a_s) > 1:
            item['m_category_name'] = a_s[1].xpath('./text()').extract_first().strip()
            item['m_category_url'] = response.urljoin(a_s[1].xpath('./@href').extract_first())
        # 图书所属小的分类
        if len(a_s) > 2:
            item['小分类名'] = a_s[2].xpath('./text()').extract_first().strip()
            item['小分类URL'] = response.urljoin(a_s[2].xpath('./@href').extract_first())
        # print(item)
        yield item
"""
{'图书URL': 'https://www.amazon.cn/dp/B07KK2488H', '图书作者': '尤四姐(作者)',y_url': 'https://www.amazon.cn/%E5%8A%A8%E6%BC%AB%E7%BB%98%E6%9C%AC-%E5%8D%A1%E9%80%9A%E6%BC%AB%E7%94%BB/b/ref=dp_bc_2?ie=UTF8&node=658403051', '图书名': '宫共4册）(晋江当红作家尤四姐最具口碑的经典之作，比肩《琅琊榜》的前朝汹涌，媲美《 '图书', '大分类URL': 'https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=dp_bc_1?F8&node=658390051', 'm_category_name': '青春动漫', '图书封面': 'https://imagesimages-amazon.com/images/I/51KlH5esgxL._SY346_.jpg'}
{'出版时间': '2014年11月1日', '图书URL': 'https://www.amazon.cn/dp/B07H9PP1VX' '王力(作者)', 'm_category_url': 'https://www.amazon.cn/%E5%8E%86%E5%8F%B2%E5%E%E4%B9%A6/b/ref=dp_bc_2?ie=UTF8&node=658418051', '图书名': '中国古代文化常识（不容错过的中国古代文化入门书，揭开古代文化神秘的面纱。）', '价格': '￥12.99 ',', '大分类URL': 'https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=dp_bc_1?ie=UTFode=658390051', 'm_category_name': '历史', '图书封面': 'https://images-cn.ssl--amazon.com/images/I/51-2haddQOL._SY346_.jpg'}

"""