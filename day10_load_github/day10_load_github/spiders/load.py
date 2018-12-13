# -*- coding: utf-8 -*-
import scrapy
import re
"""
3. 自动提交表单: 找到对应的form表单，自动解析input标签，自动解析post请求的url地址，自动带上数据，自动发送请求
   3.1 访问登录页面
   3.2 使用FormRequest.from_response方法, 来自动提交表单
"""

class LoadSpider(scrapy.Spider):
    name = 'load'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 表单所在响应
            formxpath='//*[@id="login"]/form',
            formdata={
                'login': 'CoderIvanLee',
                'password': 'lw19860404'
            },
            callback=self.login
        )

    def login(self, response):
        names = re.findall('CoderIvanLee', response.text)
        print(names)