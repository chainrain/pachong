# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64

from scrapy import signals


class Day10LearnMiddliwareDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # 创建当前类的实例对象
        s = cls()
        # 注册监听函数(回调函数),爬虫启动监听spider_opened
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # 每一个请求交给下载器之前都会调用该方法
        # Must either:
        # - return None: continue processing this request  # 继续当前的请求
        # - or return a Response object  # 如果返回响应对象, 终止当前请求, 把响应交给引擎
        # - or return a Request object  # 如果返回一个请求对象, 终止当前请求, 把请求对象交给引擎 -> 调度器
        # - or raise IgnoreRequest: process_exception() methods of  # 如果抛出IgnoreRequest异常, 将来这个异常就会经过process_exception方法, 来处理
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # 每一个响应交给下载器之前都会调用该方法
        # Must either;
        # - return a Response object  # 返回响应对象, 继续当前的请求, 就是把这个响应交给引擎
        # - return a Request object  # 返回请求对象, 终止当前请求, 把请求对象交给引擎了 -> 调度器
        # - or raise IgnoreRequest  # 抛出 IgnoreRequest. 该请求就被直接忽略
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # 用于处理下载器或下载器中间件的process_request中产生的异常.
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

"""
实现随机User-Agent的下载器中间件
步骤:
1. 在settings.py中准备User-Agent的列表
2. 定义下载器中间件类, 继承object
3. 提供一个方法, process_request, 用于给请求设置随机的User-Agent
4. 在settings.py中开启
"""

import random
from day10_learn_middliware import settings # 注意导入路径,请忽视pycharm的错误提示

class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(settings.USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent


# 随机代理中间件
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # 获取随机的代理IP
        proxy = random.choice(settings.PROXIES)
        # 获取用户名和密码
        user_passwd = proxy.get('user_passwd')
        # 如果没有用户名和密码, 直接设置request的meta属性即可
        if user_passwd is not None:
            '''如果有用户密码, 需要对用户名和密码进行base64编码'''
            user_passwd = base64.b64encode(user_passwd.encode()).decode()
            print(user_passwd)
            # 设置request的请求Proxy-Authorization属性
            request.headers['Proxy-Authorization'] = 'Basic ' + user_passwd

        # 给请求设置代理
        request.meta['proxy'] = 'http://' + proxy['ip_port']