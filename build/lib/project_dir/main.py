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

if __name__ == '__main__':
    baidu_spider = BaiduSpider()

    douban_spider = DoubanSpider()

    spiders = {
        baidu_spider.spider_name:baidu_spider,
        douban_spider.spider_name:douban_spider}
    # 1.创建引擎对象
    engine = Engine(spiders)
    # 2.调用引擎的start方法
    engine.start()