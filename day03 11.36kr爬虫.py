import requests
import re
import json

"""
获取36kr上首页的信息
# 1. 准备URL:https://36kr.com/
# 2. 发送请求获取响应数据
# 3. 解析数据
# 3.1: 使用正则表达式把页面中json数据提取出来
# 3.2: 使用json把json的字符串转换为python类型
# 4. 保存数据
"""

class KrSpider(object):
    def __init__(self):
        self.url = 'https://36kr.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def run(self):
        url = self.url
        html = self.get_html_from_url(url)
        data = self.get_data(html)
        self.save_data(data)

    def get_html_from_url(self, url):
        """获取所有数据"""
        response = requests.get(url, headers=self.headers)
        # print(response.content.decode())
        return response.content.decode()

    def get_data(self, html):
        """分析数据"""
        json_str = re.findall('<script>var props=(.+?),locationnal', html, re.S)[0]
        print(type(json_str))

        # 因为报错了:json.decoder.JSONDecodeError: Extra data: line 1 column 145258 (char 145257),所以写到文件内看一下
        # 原因:拿太多数据了,把不该拿的都拿了
        # with open('36kr.txt','w',encoding='utf-8') as f:
        #     f.write(json_str)

        # 把json的字符串转换为python类型
        data = json.loads(json_str)
        print(type(data))
        return data


    def save_data(self, data):
        """保存数据"""
        with open('36kr.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    spider = KrSpider()
    spider.run()