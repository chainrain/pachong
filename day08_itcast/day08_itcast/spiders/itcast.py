# -*- coding: utf-8 -*-
import scrapy
"""
scrapy框架还是快的啊......
比selenium快不知道多少倍了....

创建项目:
scrapy startproject 项目名
scrapy genspider 爬虫名 允许域名

运行(要在终端运行):scrapy crawl itcast --nolog
# 输出JSON格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json
# 输出JSON Lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonlines
# 输出CSV格式，使用逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv
# 输出XML格式
scrapy crawl itcast -o teachers.xml
注意,如果要写出要交给引擎 yield item,然后在管道py里面print
"""

class ItcastSpider(scrapy.Spider):
    # 爬虫名称
    name = 'itcast'
    # 允许爬取的域名,防止爬虫爬到其他网站
    allowed_domains = ['itcast.cn']
    # 爬虫从这些URL开始爬取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        """
        parse函数用于响应数据
        :param response: scrapy引擎传递过来的响应对象
        :return: 返回数据 或 请求
        """
        # response里面有xpath方法,定位需要解析的数据
        # teacher_names = response.xpath('/html/body/div[1]/div[5]/div[2]/div[10]/ul/li/div[2]/h3/text()')
        # print(teacher_names)
        # print(type(teacher_names))  # 是个<class 'scrapy.selector.unified.SelectorList'>
        # first = teacher_names.extract_first()
        # print('extract_first(): 获取第一个Selector对象中字符串数据, 如果没有就返回None',first)
        # datas = teacher_names.extract()
        # print(' extract(): 获取所有Selector对象中字符串数据, 放到列表中返回, 如果没有返回空列表',datas)
        divs = response.xpath('//div[@class="li_txt"]')  # 获取所有包含老师信息的div标签列表
        for div in divs:
            # 遍历每一个老师,获取相应数据,保存到item里
            item = {}
            item['name'] = div.xpath('./h3/text()').extract_first()
            item['level'] = div.xpath('./h4/text()').extract_first()
            item['desc'] = div.xpath('./p/text()').extract_first()
            print(item)
            # 把数据交给引擎
            # 从日志是一条一条信息输出, 说明引擎内部对数据进行遍历
            # 也就是说明, 我们只要反馈可以遍历对象, 对于引擎都是可以的.
            # 当一个爬虫, 提取数据比较多的时候, 如果都放到列表中,占用内存就会比较大, 可能会导致内存瞬间占用过高.
            # 解决方案: 就是通过yield 要返回的数据; 这样就可以避免内存瞬间占用过高的.
            yield item
