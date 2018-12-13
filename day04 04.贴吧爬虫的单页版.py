import requests
from lxml import etree
import json

"""
爬取某个贴吧里的1页帖子，获取每个帖子的标题

思路:
1. 准备URL,https://tieba.baidu.com/f?kw=吧名&mo_device=1&pn=0&
2. 发送请求, 获取响应数据
3. 解析数据, 提取需要数据
4. 保存数据
"""


class TiebaSpider(object):
    def __init__(self):
        self.name = '图拉丁'
        self.url = 'https://tieba.baidu.com/f?kw='+self.name+'&pn=0&'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }

    def run(self):
        url = self.url
        html = self.get_html(url)
        data_list = self.get_data(html)
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
            item['title'] = li.xpath('./a/div[@class="ti_title"]/span/text()')[0]
            # print(item)
            data_list.append(item)
        return data_list


    def save_data(self, data_list):
        file_name = "./test/{}.txt".format(self.name)
        with open(file_name,'a',encoding='utf-8') as f:
            for data in data_list:
                json.dump(data,f,ensure_ascii=False)
                f.write('\n')


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
