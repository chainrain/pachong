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
        
    def run(self):
        """运行方法"""
        # 1.拿到所有url
        url_list = self.get_url_list()
        # print(url_list)
        # 2.遍历得到每一个url,发送请求
        for url in url_list:
            # 每个url的页面数据
            html = self.get_html(url)
            # 拿到人头像URL,昵称,性别,段子内容, 好笑数,评论数
            data_list = self.get_data(html)
            # 保存数据
            self.save_data(data_list)

    def get_url_list(self):
        # return [self.url.format(i) for i in range(1,14)]  # 列表生成式
        url_list = []
        for i in range(1,14):  # 最多13页
            url_list.append(self.url.format(i))
        return url_list

    def get_html(self, url):
        html = requests.get(url,headers=self.headers)
        return html.content.decode()

    def get_data(self, html):
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
                item['gender'] = re.findall('(\w+)Icon',gender_class[0])[0]
            else:
                item['gender']= None
            # 段子内容,本来是个列表,用.join转
            item['content'] = ''.join(div.xpath('./a/div/span//text()'))
            # 好笑数
            item['vote_count'] = div.xpath('.//span[@class="stats-vote"]/i/text()')[0]
            # 评论数
            item['comments_count'] = div.xpath('.//span[@class="stats-comments"]/a/i/text()')[0]
            # print(item)
            data_list.append(item)
        # 返回数据
        print(data_list)
        return data_list

    def save_data(self, data_list):
        """ 保存数据"""
        with open('./test/糗事热门.jsonlines', 'a') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')


if __name__ == '__main__':
    spider = QiushiSpider()
    spider.run()