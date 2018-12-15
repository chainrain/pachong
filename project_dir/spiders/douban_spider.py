"""
### 4. 实现豆瓣电影Top250爬虫, 测试多请求
- `目标`: 实现豆瓣电影Top250爬虫, 来测试多请求
- `步骤`:
   - 在项目文件夹下的spiders包中, 创建douban_spider.py文件, 定义DoubanSpider类, 继承Spider
   - 重写start_requests方法, 构建起始请求

分析:
 URL规律:
 第1页: https://movie.douban.com/top250?start=0&filter=
 第2页: https://movie.douban.com/top250?start=25&filter=
 第3页: https://movie.douban.com/top250?start=50&filter=
 一共10页
 URL规律明显, 并且页数固定的, 可以生成UR列表

8.1.2 修改项目中douban和baidu爬虫, 增加spider_name属性
"""
from day13_ScrapyPlus.core.spider import Spider
from day13_ScrapyPlus.http.request import Request
from day13_ScrapyPlus.item import Item


class DoubanSpider(Spider):
    spider_name = 'douban'

    # start_urls = []
    #  - 重写start_requests方法, 构建起始请求
    def start_requests(self):
        """构建多个起始请求"""
        # 准备url模板
        url_pattern = 'https://movie.douban.com/top250?start={}&filter='
        for i in range(0, 250, 25):
            url = url_pattern.format(i)
            # 构建请求对象, 交给引擎
            yield Request(url)

    def parse(self, response):
        """实现豆瓣top250列表页的数据解析"""
        # 获取包含电影信息的li标签列表
        lis = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # 遍历lis, 获取数据
        for li in lis:
            item = {}
            item['movie_name'] = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
            item['movie_url'] = li.xpath('./div/div[2]/div[1]/a/@href')[0]
            # yield Item(item)
            # print(item)
        # return Item(response.url)
            # 构建详情页的请求
            yield Request(item['movie_url'], callback=self.parse_movie_detial,meta={'item': item} )

    def parse_movie_detial(self, response):
        """取出传递过来的数据"""
        item = response.meta['item']
        print(item)

        return Item(response.url)
