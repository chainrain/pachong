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
    # 1.创建引擎对象
    engine = Engine(douban_spider)
    # 2.调用引擎的start方法
    engine.start()