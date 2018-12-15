"""
响应模块:用于封装一个响应数据
"""
import json
import re

from lxml import etree


class Response(object):
    def __init__(self,url,status_code=200,headers={},body=None):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def xpath(self, path):
        """
        使用XPATH提取数据
        :param path:  XPATH的路径表达式
        :return: 返回XPATH的结果, 是一个列表
        """
        # 1. 调用lxml的etree.HTML(响应数据)
        element = etree.HTML(self.body)
        # 2. 使用XPATH提取数据, 并返回
        return element.xpath(path)

    def json(self):
        """
        2. 实现Response支持json方法, 使用json模块, 解析数据; 前提响应必须是json格式字符串
        :return: 字典
        """
        return json.loads(self.body.decode())

    def findall(self, pattern, content=None):
        """
         #  3. 实现Response支持findall, 使用re模块findall来实现的;
        :param pattern: 正则表达式
        :param content: 要解析内容, 如果没有就使用响应数据
        :return:
        """
        if content is None:
            content = self.body.decode()
        # 返回正则findall方法的匹配结果
        return re.findall(pattern, content)