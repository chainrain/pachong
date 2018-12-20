"""
需求: 获取获取热映电影信息, 保存到文件中

1. 准备URL: json格式数据的URL
url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1543306858016'
# start: 起始索引号/偏移量
# count: 每次请求返回多少条数据
2. 发送请求, 获取响应数据
3. 解析响应数据
4. 保存数据
"""
import json

import requests


class DoubanSpider(object):
    def __init__(self):
        """准备参数"""
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1543306858016'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288'
        }

    def run(self):
        # 获取响应数据
        html = self.get_page_from_url()
        print(html)  # 得到json字符串
        # 分析响应数据
        movie_list = self.get_movie_list(html)
        # 保存数据
        self.save_data(movie_list)

    def get_page_from_url(self):
        """获取响应数据"""
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()


    def get_movie_list(self, html):
        """分析响应数据"""
        data = json.loads(html)
        # print(data)  # 转python数据
        movie_list = data['subject_collection_items']
        # print(movie_list)
        return movie_list


    def save_data(self, movie_list):
        """保存数据"""
        with open('04_douban.txt','w',encoding='utf-8') as f:
            for movie in movie_list:
                json.dump(movie,f,ensure_ascii=False)
                f.write('\n')


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
