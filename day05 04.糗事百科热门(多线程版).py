from queue import Queue
from threading import Thread

import requests
from lxml import etree
import re
import json

"""
需求: 提取糗百中热门主题中所有段子信息,每个段子包含发送人头像URL,昵称,性别,段子内容, 好笑数,评论数

URL有规律
第1页: https://www.qiushibaike.com/8hr/page/1/
第2页: https://www.qiushibaike.com/8hr/page/2/
第3页: https://www.qiushibaike.com/8hr/page/3/
# 一共就13页, 页数是固定.
# 我们可以给他生成URL列表

思路:
1. 准备URL列表
2. 遍历URL列表, 发送请求, 获取响应
3. 解析数据(重点)
4. 保存数据
"""


class QiushiSpider(object):
    def __init__(self):
        """准备初始化参数"""
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.url_queue = Queue()
        self.page_queue = Queue()
        self.data_queue = Queue()

    def run(self):
        """运行方法"""
        #  6. 创建几个线程, 执行2,3,4,5.
        self.execute_task(self.add_url_to_queue)
        self.execute_task(self.add_html_to_queue, 2)
        self.execute_task(self.add_data_to_queue)
        self.execute_task(self.save_data)
        # 等待队列任务完成
        self.url_queue.join()
        self.page_queue.join()
        self.data_queue.join()

    def add_url_to_queue(self):
        """
        2. 修改get_url_list, 该为add_url_to_queue, 用于把URL添加到URL队列url_queue中
        """
        for i in range(1, 14):  # 最多13页
            url = self.url.format(i)
            self.url_queue.put(url)


    def add_html_to_queue(self):
        """
        3. 修改get_page_from_url, 该为add_page_to_queue,
        用于从URL队列中取出URL, 发送请求获取响应,把数据放到响应队列中
        """
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            html = response.content.decode()
            self.page_queue.put(html)
            self.url_queue.task_done()  # 结束一个url的任务

    def add_data_to_queue(self):
        """
        4. 修改get_data_from_page, 该为add_data_to_queue,
        用于从响应队列中取出页面数据,解析数据, 把提取出来的数据, 添加到数据队列中
        """
        while True:
            html = self.page_queue.get()
            element = etree.HTML(html)
            # 定位到所有端子列表
            divs = element.xpath('//*[@id="content-left"]/div')
            data_list = []
            for div in divs:
                item = {}
                # 头像
                item['head_img'] = div.xpath('./div[1]/a[1]/img/@src')
                # 头像路径
                item['head_img'] = 'https:' + item['head_img'][0] if len(item['head_img']) != 0 else None
                # 昵称
                item['nick_name'] = div.xpath('./div[1]/a[2]/h2/text()')
                # strip(): 去掉两端空白符
                item['nick_name'] = item['nick_name'][0].strip() if len(item['nick_name']) != 0 else None
                # 性别
                gender_class = div.xpath('./div[1]/div/@class')
                if len(gender_class) != 0:
                    item['gender'] = re.findall('(\w+)Icon', gender_class[0])[0]
                else:
                    item['gender'] = None
                # 段子内容,本来是个列表,用.join转
                item['content'] = ''.join(div.xpath('./a/div/span//text()'))
                # 好笑数
                item['vote_count'] = div.xpath('.//span[@class="stats-vote"]/i/text()')[0]
                # 评论数
                item['comments_count'] = div.xpath('.//span[@class="stats-comments"]/a/i/text()')[0]
                # print(item)
                data_list.append(item)
            # 把提取出来的数据, 添加到数据队列中
            self.data_queue.put(data_list)
            # 页面队列任务完成了
            self.page_queue.task_done()

    def save_data(self):
        """ 5. 修改save_data,  用于从数据队列中取出数据, 进行保存"""
        while True:
            data_list = self.data_queue.get()
            with open('./test/糗事热门.jsonlines', 'a') as f:
                for data in data_list:
                    json.dump(data, f, ensure_ascii=False)
                    f.write('\n')
            self.data_queue.task_done()

    def execute_task(self, task, count=1):
        """
        使用线程执行任务
        :param task:  要执行任务函数(方法)
        :param count:  开启多少个线程来执行
        """
        for i in range(count):
            t = Thread(target=task)
            t.setDaemon(True)
            t.start()

if __name__ == '__main__':
    spider = QiushiSpider()
    spider.run()
