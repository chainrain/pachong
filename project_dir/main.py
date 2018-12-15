# from day13_ScrapyPlus.core.engine import Engine
#
# if __name__ == '__main__':
#     # 1.创建引擎对象
#     engine = Engine()
#     # 2.调用引擎的start方法
#     engine.start()


from day13_ScrapyPlus.core.engine import Engine
from spiders.baidu_spider import BaiduSpider
from spiders.douban_spider import DoubanSpider

from pipelines import BaiduPipeline,DoubanPipeline

from middlewares.downloader_middlewares import DownloaderMiddleware1,DownloaderMiddleware2
from middlewares.spider_middlewares import SpiderMiddleware1,SpiderMiddleware2

if __name__ == '__main__':
    baidu_spider = BaiduSpider()

    douban_spider = DoubanSpider()

    spiders = {
        baidu_spider.spider_name:baidu_spider,
        douban_spider.spider_name:douban_spider}

    pipelines = [
        BaiduPipeline(),
        DoubanPipeline()
    ]

    # 下载中间件列表
    downloader_middlewares = [
        DownloaderMiddleware1(),
        DownloaderMiddleware2()
    ]

    # 爬虫中间件列表
    spider_middlewares = [
        SpiderMiddleware1(),
        SpiderMiddleware2()
    ]
    # 1.创建引擎对象
    engine = Engine(spiders,pipelines,downloader_middlewares,spider_middlewares)
    # 2.调用引擎的start方法
    engine.start()