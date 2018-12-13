 # -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
"""
CrawlSpider帮我们做了什么：
从response中提取所有的满足规则的url地址
自动的构造自己requests请求，发送给引擎
对应的crawlspider就可以实现上述需求，能够匹配满足条件的url地址，组装成Reuqest对象后自动发送给引擎，同时能够指定callback函数,来处理该Request对应的响应数据
即：crawlspider爬虫可以按照规则自动获取连接

- 作用: 根据规则自动从响应中,提取URL, 如果URL不全, 会自动补全; 构建请求对象, 交给引擎
- 使用:
  - 创建crawlspider爬虫: scrapy genspider -t crawl 爬虫名称  允许的域名
  - 完善爬虫:
    - 完善提取URL规则
    - 完善解析函数
- 注意点:
  - crawlspider中不能再有以parse为名的数据提取方法
  - Rule对象中LinkExtractor为固定参数，其他callback、follow为可选参数
  - 如果连接被前面的rule(规则)提取了, 它就不会经过后面的规则了
  - 不同规则直接无法进行数据传递, 但是在解析函数中可以构建请求, 传递数据的.

- 规则的使用
    - crawlspider中rules的使用：
    - rules是一个元组或者是列表，包含的是Rule对象
    - Rule表示规则，其中包含LinkExtractor,callback和follow等参数
    - LinkExtractor:连接提取器，可以通过正则或者是xpath来进行url地址的匹配
    - callback :表示经过连接提取器提取出来的url地址响应的回调函数，可以没有，没有表示响应不会进行回调函数的处理
    - follow：连接提取器提取的url地址对应的响应是否还会继续被rules中的规则进行提取，True表示会，Flase表示不会

步骤:
scrapy startproject 项目名
scrapy genspider -t crawl 爬虫名 允许域名(scrapy genspider -t crawl zhaopin tencent.com)
"""

class ZhaopinSpider(CrawlSpider):
    name = 'zhaopin'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # follow 要不要从下一个页面重复提取(可选的,不加默认为false)
        # callback: 用于解析(处理)链接提取器提取出来链接对应响应数据的(可选的), 指定指定为一个字符串.
        # 注意,最后要加逗号,不然builtins.TypeError: 'Rule' object is not iterable


        # 找到所有的下一页页面,按url规则找,方式一:
        # Rule(LinkExtractor(allow=r'position.php\?&start=\d+#a'), callback='parse_item', follow=False),

        # 找到所有的下一页页面,按xpaths定位,方式二:
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="pagenav"]'),callback='parse_item',follow=False),

        # 提取详情页url
        Rule(LinkExtractor(allow='position_detail.php'),callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        print(response.url)

