import datetime

from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
from ..http.request import Request
from ..middlewares.spider_middlewares import SpiderMiddleware
from ..middlewares.downloader_middlewares import DownloaderMiddleware

"""
引擎模块:调度各个模块,实现各个模块间数据的传递
实现思路:
1.初始化爬虫,调度器,下载器,管道
2.提供启动爬虫的方法
3.提供一个私有启动的方法,用于封装框架运行的核心

每一次修改代码都要重新安装python3 setup.py install
"""


class Engine(object):
    def __init__(self):
        """
        初始化爬虫,调度器,下载器,管道
        """
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        # 中间件
        self.spider_middleware = SpiderMiddleware()
        self.downloader_middleware = DownloaderMiddleware()

    def start(self):
        """
            2.提供一个外界启动爬虫框架的方法
        """
        self.__start()

    def __start(self):
        """
        一个私有方法,用于封装框架运行的核心逻辑
        :return:
        """
        # 1.调用爬虫start_requests,获取起始请求
        request = self.spider.start_requests()
        request = self.spider_middleware.process_request(request)  # 爬虫中间件
        # 2.调用调度器的add_request方法,把请求放到调度器中
        self.scheduler.add_request(request)
        # 3.调用调度器的get_request方法,获取请求对象
        request = self.scheduler.get_request()
        request = self.downloader_middleware.process_request(request)  # 下载中间件,对请求进行处理

        # 4.调用下载器的get_response的方法
        response = self.downloader.get_response(request)
        response = self.downloader_middleware.process_response(response)  # 调用下载中间件的process_response方法,对响应进行处理
        response = self.spider_middleware.process_response(response)  # 在把响应数据交给爬虫之前,先经过爬虫中间进行处理
        # 5.调用爬虫模块的parse函数,解析响应数据,获取解析结果
        result = self.spider.parse(response)
        # 如果是请求,添加到调度器中,否则,把处理结果交给管道
        if isinstance(result,Request):
            result = self.spider_middleware.process_request(result)  # 如果解析是请求,就用爬虫中间件对请求进行处理
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(item=result,spider=self.spider)