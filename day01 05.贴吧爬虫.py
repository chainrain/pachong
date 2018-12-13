import requests
"""
实现任意贴吧的爬虫,保存网页到本地;
  要求: 可以指定贴吧名称, 起始页与结束页
URL规律
第1页:  http://tieba.baidu.com/f?kw=吧名&ie=utf-8&pn=0
第2页:  http://tieba.baidu.com/f?kw=吧名&ie=utf-8&pn=50
第3页:  http://tieba.baidu.com/f?kw=吧名&ie=utf-8&pn=100

1. 准备URL列表
2. 发送请求, 获取响应数据
3. 保存数据
"""


class TiebaSpider(object):
    def __init__(self,name,start,end):
        """初始化"""
        self.name = name
        self.start = start
        self.end = end
        # 搜索模板
        self.url = 'http://tieba.baidu.com/f?kw=' + name + '&ie=utf-8&pn={}'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def run(self):
        """程序主入口"""
        url_list = self.get_url_list()  # 从get_url_list拿到url列表
        # print(url_list)
        page = self.start  # 页码
        for url in url_list:
            """遍历url列表"""
            response = self.get_response_from_url(url)  # 把url传到get_response_from_url里
            self.save_response(response,page)  # 因为get_response_from_url函数return response.content.decode(),传给save_response,所以传给save_response就用response写入就行.自增页码传给save_response,写入文件名字
            page += 1  # page自增

    def get_url_list(self):
        """url列表"""
        url_list = []
        for page in range(self.start,self.end+1):
            url = self.url.format((page-1)*50)  # 第一页0,第二页50,第三页100
            url_list.append(url)
        return url_list

    def get_response_from_url(self, url):
        """根据URL,获取响应数据"""
        response = requests.get(url=url,headers=self.headers)
        return response.content.decode()

    def save_response(self, response, page):
        """保存页面数据"""
        file = '/home/python/Desktop/pachong/test/{}_第{}页.test'.format(self.name,page)
        with open(file,'w',encoding='utf-8') as f:
            f.write(response)


if __name__ == '__main__':
    name = input('贴吧名字')
    start = int(input('开始页码'))
    end = int(input('结束页码'))
    tbs = TiebaSpider(name,start,end)  # 三个参数.吧名,开始页数,结束页数
    tbs.run()