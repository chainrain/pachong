"""
需求: 获取获取热映电影信息, 保存到文件中

1. 准备URL: json格式数据的URL
url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1543306858016'
# start: 起始索引号/偏移量
# count: 每次请求返回多少条数据
2. 发送请求, 获取响应数据
3. 解析响应数据
4. 保存数据

总结:
  1.修改init中URL, 使用{}对 start={} 占位
  2. get_movie_list_from_page, 计算下一页的URl ,如果没有就返回None
  3. 修改run方法
     url = self.url.format(0)
     while url:
        ....
        movie_list, url = self.get_movie_list_from_page(page)
  4. 修改save_data, 把写入模式 由 'w' 改为 'a'
"""

import json

import requests


class DoubanSpider(object):
    def __init__(self):
        """准备参数"""
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1543306858016'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288'
        }

    def run(self):
        next_url = self.url.format(0)

        while next_url:
            # 获取响应数据
            html = self.get_page_from_url(next_url)
            # print(test)  # 得到json字符串
            # 分析响应数据
            movie_list,next_url = self.get_movie_list(html)

            # 保存数据
            self.save_data(movie_list)


    def get_page_from_url(self,url):
        """获取响应数据"""
        response = requests.get(url,headers=self.headers)
        return response.content.decode()


    def get_movie_list(self, html):
        """分析响应数据"""
        data = json.loads(html)
        # print(data)  # 转python数据
        movie_list = data['subject_collection_items']
        # print(movie_list)

        # 读取数据里面的start(初始号)
        start = data['start']
        # 读取数据里面的count(本次请求的条数)
        count = data['count']
        # 读取数据里面的total(总条数)
        total = data['total']
        # 计算下一页
        next_page = start + count
        # 如果next_page<total, 说明有下一页,比如一个48条,第2页是36条,小于总数48条
        if next_page < total:
            next_url = self.url.format(next_page)
        else:
            next_url = None

        return movie_list,next_url


    def save_data(self, movie_list):
        """保存数据"""
        with open('06_douban.txt','a',encoding='utf-8') as f:
            for movie in movie_list:
                json.dump(movie,f,ensure_ascii=False)
                f.write('\n')



if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
    print('done')

