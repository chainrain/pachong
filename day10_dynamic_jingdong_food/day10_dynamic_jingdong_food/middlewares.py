# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

"""
Selenium+scrapy使用的一般步骤:
1. 定义Selenium的下载器中间件类
1.1  from_crawler 注册 爬虫启动和爬虫关闭监听函数
1.2 当爬虫打开的时候, 创建浏览器驱动
1.3 当爬虫关闭时候, 退出浏览器
1.4 在process_requests:
    - 发送需要使用selenium处理的请求的时候, 就使用selenium加载页面进行处理
    - 把渲染后的内容封装为HtmlResponse反会给引擎
2. 在settings.py中开启该类

"""


from scrapy import signals
from selenium import webdriver
# 导入封装HtmlResponse的类
from scrapy.http.response.html import HtmlResponse
import time

class Day10DynamicJingdongFoodDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    """
    遇到数据是动态生成的,不想过多的操作,可以用中间件加selenium+中间件来做
    1. 当爬虫启动的时候, 创建驱动对象
    2. 当前爬虫关闭的时候, 退出浏览器
    3. 在处理请求的时候, 使用驱动发送请求
    """
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        # 注册监听函数, 当爬虫启动使用调用spider_opened
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        # 注册监听函数, 当爬虫关闭的时候执行spider_closed
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)


        return s

    def spider_opened(self, spider):
        """当爬虫启动的时候执行"""
        if spider.name == 'dynamic_food':
            #  1. 当爬虫启动的时候, 创建驱动对象
            self.driver = webdriver.Chrome()

    def spider_closed(self, spider):
        """当爬虫关闭的时候执行"""
        # 当前爬虫关闭的时候, 退出浏览器
        if spider.name == 'dynamic_food':
            self.driver.quit()

    def process_request(self, request, spider):
        # 我们使用selenium加载页面, 获取渲染后的数据, 封装Response返回给引擎
        if spider.name == 'dynamic_food':
            # 使用浏览器加载请求URL
            self.driver.get(request.url)
            time.sleep(1)
            # 获取渲染后的页面内容
            text = self.driver.page_source
            # 把渲染后的内容, 封装Response返回给引擎
            return HtmlResponse(
                url=self.driver.current_url,
                body=text,
                encoding='UTF-8',
                request=request
            )

        return None


