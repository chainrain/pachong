from day13_ScrapyPlus.core.spider import Spider


class BaiduSpider(Spider):
    # start_url = 'http://www.hao123.com'
    spider_name = 'baidu'
    # 修改项目中douban和baidu爬虫, 增加spider_name属性
    start_urls = ['http://www.hao123.com', 'http://www.baidu.com','http://www.hao123.com']
