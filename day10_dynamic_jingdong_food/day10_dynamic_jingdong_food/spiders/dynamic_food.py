"""Selenium+scrapy,得到渲染后的数据"""
# -*- coding: utf-8 -*-
# import scrapy
#
# from scrapy_splash import SplashRequest  # scrapy_splash的使用
#
#
# class DynamicFoodSpider(scrapy.Spider):
#     name = 'dynamic_food'
#     allowed_domains = ['jd.com']
#     start_urls = ['https://channel.jd.com/food.html']
#
#     def parse(self, response):
#         # 进口牛奶,因为是动态的所以拿不到
#         food = response.xpath('//*[@id="food_banner_2"]/div[1]/div[2]/div[1]/div[1]/p/a[1]/text()').extract_first()
#         print(food)


"""
scrapy_splash的使用
注意,要使用这个的话,要把splash开启来:
sudo docker run -p 8050:8050 scrapinghub/splash
"""
# -*- coding: utf-8 -*-
import scrapy

# 导入SplashRequest
from scrapy_splash.request import SplashRequest


class FoodSpider(scrapy.Spider):
    name = 'dynamic_food'
    allowed_domains = ['jd.com']
    # start_urls = ['https://channel.jd.com/food.html']

    def start_requests(self):
        # 重写  start_requests 构建 SplashRequest 的请求
        yield SplashRequest(
            url='https://channel.jd.com/food.html',
            callback=self.parse,
            args={'wait': 0.5}, # 由于splash渲染需要时间, 此处需要等待0.5s
        )

    def parse(self, response):
       food = response.xpath('//*[@id="food_banner_2"]/div[1]/div[2]/div[1]/div[1]/p/a[1]/text()').extract_first()
       print(food)
