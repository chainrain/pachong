"""
爬虫模块,
1.准备起始URL
2.解析响应数据(提取数据,提取URL)
"""

from ..http.request import Request
from ..item import Item


class Spider(object):
    # 起始URL
    start_url = 'http://www.baidu.com'

    def start_requests(self):
        """
        准备起始请求
        :return:
        """
        # 根据起始URL,构建一个请求,交给引擎
        return Request(self.start_url)

    def parse(self, response):
        print(response.body.decode())
        return Item(response.url)
