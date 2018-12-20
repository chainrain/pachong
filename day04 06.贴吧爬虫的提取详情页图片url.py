import re

import requests
from lxml import etree
import json

"""
爬取某个贴吧里的所有帖子,和帖子中图片

思路:
1. 准备URL,https://tieba.baidu.com/f?kw=吧名&mo_device=1&pn=0&
2. 发送请求, 获取响应数据
3. 解析数据, 提取需要数据
4. 保存数据

列表页的分页
URL规律:
第1页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=0&
第2页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=50&
第3页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=100&
"""


class TiebaSpider(object):
    def __init__(self):
        self.name = '图拉丁'
        self.url = 'https://tieba.baidu.com/f?kw='+self.name+'&pn={}&'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }
        # 贴吧域名(用于补全URL)
        self.tieba_url = 'https://tieba.baidu.com'

    def run(self):
        next_url = self.url
        while next_url:
            html = self.get_html(next_url)
            data_list,next_url = self.get_data(html)
            self.save_data(data_list)

    def get_html(self, url):
        """发送请求,得到数据"""
        html = requests.get(url=url,headers=self.headers)
        # print(test.content.decode())
        return html.content.decode()

    def get_data(self, html):
        """解析内容"""
        element = etree.HTML(html)
        li_list = element.xpath('//li[@class="tl_shadow tl_shadow_new"]')
        # print(len(li_list))
        data_list = []
        for li in li_list:
            item = {}
            item['title'] = li.xpath('./a/div[@class="ti_title"]/span/text()')
            item['detail_url'] = self.tieba_url + li.xpath('./a/@href')[0]
            item['imgs'] = self.get_imgs(item['detail_url'])
            # print(item)
            data_list.append(item)

        # 从html源码中提取"page_size":一页多少条
        page_size = int(re.findall('"page_size":(\d+)',html)[0])
        # 从html源码中提取"current_page":当前页号
        current_page = int(re.findall('"current_page":(\d+)',html)[0])
        # 从html源码中提取"total_page":总页数
        total_page = int(re.findall('"total_page":(\d+)',html)[0])
        # 如果有下一页,就生成下一页URL
        if current_page < total_page:
            next_url = self.url.format(current_page * page_size)
        else:
            next_url = None
        print(next_url)
        return data_list,next_url


    def save_data(self, data_list):
        file_name = "./test/{}.txt".format(self.name)
        with open(file_name,'a',encoding='utf-8') as f:
            for data in data_list:
                json.dump(data,f,ensure_ascii=False)
                f.write('\n')

    def get_imgs(self, detail_url):

        # print(detail_url_pattern)

        while True:
            detail_url_pattern = detail_url + '&pn={}'
            imgs = []
            # 发送数据,获取每个贴的响应数据
            detail_page = self.get_html(detail_url)
            # 每个贴的响应对象
            element = etree.HTML(detail_page)
            # print(element)
            # 每个贴的图片
            img_urls = element.xpath('//div[@data-class="BDE_Image"]/@data-url')
            # print(img_urls)
            # 解码变高清大图
            for img_url in img_urls:
                img_url = requests.utils.unquote(img_url)
                img_url = img_url.split('src=')[1]
                imgs.append(img_url)
            page_sizes = re.findall('"page_size":(\d+)', detail_page)

            # 从html源码中提取"page_size":一页多少条
            page_size = int(page_sizes[0])
            # 从html源码中提取"current_page":当前页号
            current_page = int(re.findall('"current_page":(\d+)', detail_page)[0])
            # 从html源码中提取"total_page":总页数
            total_page = int(re.findall('"total_page":(\d+)', detail_page)[0])
            # 如果有下一页,就生成下一页URL
            if current_page < total_page:
                detail_url = detail_url_pattern.format(current_page * page_size)
            else:
                break
        print(imgs)
        return imgs


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
