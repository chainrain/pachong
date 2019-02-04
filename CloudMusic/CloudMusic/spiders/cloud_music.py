# -*- coding: utf-8 -*-
import scrapy


class CloudMusicSpider(scrapy.Spider):
    name = 'cloud_music'
    allowed_domains = ['https://music.163.com']
    start_urls = ['https://music.163.com/#/discover/artist/signed/']

    def parse(self, response):
        print(response.text)
        all_singer = response.xpath('//*[@id="m-artist-box"]')
        #print(all_singer)
        yield

