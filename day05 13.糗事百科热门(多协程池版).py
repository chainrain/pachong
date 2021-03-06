# 打猴子补丁(热补丁) : 可以自动在等待, IO操作, 网络等位置自动添加协程间切换代码
from gevent import monkey
monkey.patch_all()

# 把导入线程池, 改为导入协程池,
from gevent.pool import Pool
from queue import Queue

import time
from lxml import etree
import requests
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

# 实现多线程版的爬虫
1. 初始URL队列, 响应队列, 数据队列, 在init方法中
2. 修改get_url_list, 该为add_url_to_queue, 用于把URL添加到URL队列中
3. 修改get_page_from_url, 该为add_page_to_queue, 用于从URL队列中取出URL, 发送请求获取响应,把数据放到响应队列中
4. 修改get_data_from_page, 该为add_data_to_queue, 用于从响应队列中取出页面数据,解析数据, 把提取出来的数据, 添加到数据队列中
5. 修改save_data, 用于从数据队列中取出数据, 进行保存
6. 创建几个线程, 执行2,3,4,5.

# 把多线程版该为线程池版
1. 把线程改为线程池
1.1 把导入线程, 改为导入线程池
1.2 在init方法中, 创建线程池对象
1.3 修改excute_task使用线程池执行异步任务
1.4 等待, 让线程的异步任务能够开始执行
注意:
   线程池中线程的个数必须大于等待死循环任务个数, 否则就可能会导致整个程序无法结束, 有些任务执行不了

# 把线程池版改为协程池版
1. 把导入线程池, 改为导入协程池, 并打猴子补丁
注意:
   猴子补丁必须在导入requests模块之前打
   建议: 猴子补丁要尽可能早的打.
"""


class QiushiSpider(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        # 三大队列,进程队列要使用JoinableQueue
        self.url_queue = Queue()  # type:Queue
        self.page_queue = Queue()  # type:Queue
        self.data_queue = Queue()  # type:Queue
        # 线程池
        self.pool = Pool(5)  # 要多过任务的数量,不然会卡线程

    def run(self):
        # 执行任务
        self.excute_task(self.add_url)
        self.excute_task(self.add_page,2)
        self.excute_task(self.add_data)
        self.excute_task(self.save_data)

        # 等待队列任务完成
        time.sleep(0.1)  # 让线程异步任务能够开始执行
        self.url_queue.join()
        self.page_queue.join()
        self.data_queue.join()

    def excute_task(self, task, count=1):
        """
        使用线程执行任务
        :param task:  要执行任务函数(方法)
        :param count:  开启多少个线程来执行
        """
        for i in range(count):
            self.pool.apply_async(task)  # 线程池异步执行

    def add_url(self):
        """获取url列表,添加到url_queue队列"""
        for i in range(1, 14):
            url = self.url.format(i)
            self.url_queue.put(url)

    def add_page(self):
        """从url_queue获取url的页面,添加到page_queue队列"""
        while True:
            url = self.url_queue.get()
            response = requests.get(url=url, headers=self.headers)
            page = response.content.decode()
            self.page_queue.put(page)
            self.url_queue.task_done()  # 表明url队列已完成

    def add_data(self):
        """从page_queue获取页面,解析页面,添加到data_queue队列"""
        while True:
            page = self.page_queue.get()
            print(page)
            element = etree.HTML(page)
            print('element',element)
            divs = element.xpath('//*[@id="content-left"]/div')  # 所有段子信息
            # print('divs',divs)
            data_list = []
            for div in divs:
                """遍历divs,拿到每一个段子的div,然后把想要的数据保存在data_list中"""
                item = {}
                # 用户头像
                item['head_img'] = div.xpath('./div[1]/a[1]/img/@src')
                item['head_img'] = 'https:' + item['head_img'][0] if len(item['head_img']) != 0 else None
                # 昵称
                item['nick_name'] = div.xpath('./div[1]/a[2]/h2/text()')
                item['nick_name'] = item['nick_name'][0].strip() if len(item['nick_name']) != 0 else None
                # 性别
                gender_class = div.xpath('./div[1]/div/@class')
                if len(gender_class) != 0:  # 判断是否有填写性别
                    # articleGender womenIcon
                    item['gender'] = re.findall('(\w+)Icon', gender_class[0])[0]
                else:
                    item['gender'] = None
                # 段子内容
                item['content'] = ''.join(div.xpath('./a/div/span//text()'))
                # 好笑数
                item['vote_count'] = div.xpath('.//span[@class="stats-vote"]/i/text()')[0]
                # 评论数
                item['comments_count'] = div.xpath('.//span[@class="stats-comments"]/a/i/text()')[0]
                # print(item)
                data_list.append(item)
            self.data_queue.put(data_list)  # 添加到data队列
            self.page_queue.task_done()  # 表明page队列已完成

    def save_data(self):
        """从data_queue拿到数据保存"""
        while True:
            data_list = self.data_queue.get()
            with open('./test/糗事百科热门(多协程池版).jsonlines', 'a', encoding='utf-8') as f:
                for data in data_list:
                    json.dump(data, f, ensure_ascii=False)
                    f.write('\n')
            self.data_queue.task_done()  # 完成数据队列任务


if __name__ == '__main__':
    spider = QiushiSpider()
    spider.run()
