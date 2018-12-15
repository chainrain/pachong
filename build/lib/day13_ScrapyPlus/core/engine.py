import datetime

from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
from ..http.request import Request
from ..middlewares.spider_middlewares import SpiderMiddleware
from ..middlewares.downloader_middlewares import DownloaderMiddleware
from ..utils.log import logger

"""
引擎模块:调度各个模块,实现各个模块间数据的传递
实现思路:
1.初始化爬虫,调度器,下载器,管道
2.提供启动爬虫的方法
3.提供一个私有启动的方法,用于封装框架运行的核心

每一次修改代码都要重新安装python3 setup.py install
"""


class Engine(object):
    def __init__(self,spider):
        """
        初始化爬虫,调度器,下载器,管道
        """
        self.spider = spider
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        # 中间件
        self.spider_middleware = SpiderMiddleware()
        self.downloader_middleware = DownloaderMiddleware()
        self.total_response_num = 0

    def start(self):
        """
            2.提供一个外界启动爬虫框架的方法
        """
        # 开始时间
        start = datetime.datetime.now()
        logger.info('开始运行的时间:{}'.format(start))
        self.__start()
        # 结束时间
        end = datetime.datetime.now()
        logger.info('结束运行的时间:{}'.format(end))
        # 总耗时
        logger.info('总耗时:{}秒'.format((end-start).total_seconds()))

    def __start(self):
        """
        一个私有方法,用于封装框架运行的核心逻辑
        :return:
        """
        self.__add_start_requests()  # 3.调用调度器的get_request方法,获取请求对象
        while True:
            self.__execute_request_response_item()
            if self.total_response_num >= self.scheduler.total_request_num:
                break

    def __execute_request_response_item(self):
        request = self.scheduler.get_request()
        request = self.downloader_middleware.process_request(request)  # 下载中间件,对请求进行处理
        # 4.调用下载器的get_response的方法
        response = self.downloader.get_response(request)
        response = self.downloader_middleware.process_response(response)  # 调用下载中间件的process_response方法,对响应进行处理
        response = self.spider_middleware.process_response(response)  # 在把响应数据交给爬虫之前,先经过爬虫中间进行处理
        # 5.调用爬虫模块的parse函数,解析响应数据,获取解析结果
        result = self.spider.parse(response)
        # 如果是请求,添加到调度器中,否则,把处理结果交给管道
        if isinstance(result, Request):
            result = self.spider_middleware.process_request(result)  # 如果解析是请求,就用爬虫中间件对请求进行处理
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(item=result, spider=self.spider)
        self.total_response_num += 1

    def __add_start_requests(self):
        # 1.调用爬虫start_requests,获取起始请求
        for request in self.spider.start_requests():
            # 遍历爬虫中间件的process_request来处理请求
            request = self.spider_middleware.process_request(request)  # 爬虫中间件
            # 2.调用调度器的add_request方法,把请求放到调度器中
            self.scheduler.add_request(request)