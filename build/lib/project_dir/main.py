# from day13_ScrapyPlus.core.engine import Engine
#
# if __name__ == '__main__':
#     # 1.创建引擎对象
#     engine = Engine()
#     # 2.调用引擎的start方法
#     engine.start()


from day13_ScrapyPlus.core.engine import Engine
from spiders.baidu_spider import BaiduSpider

if __name__ == '__main__':
    baidu_spider = BaiduSpider()
    # 1.创建引擎对象
    engine = Engine(baidu_spider)
    # 2.调用引擎的start方法
    engine.start()