from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import json

class ZuFangSpider(object):

    def __init__(self):
        #  1. 准备起始URL
        self.url = 'https://gz.58.com/chuzu/'
        #  7. 实现无界面的浏览器
        options = Options()
        options.headless = True
        #  2. 创建driver对象
        self.driver = webdriver.Chrome(options=options)

    def get_data(self):
        """提取数据, 返回数据列表"""
        # 我们也是使用XPATH语法提取数据, 使用原则都是一样的
        # 1. 先分组, 获取包含所有租房信息的li标签列表
        # 倒数第一个li标签是分页, 倒数第二是广告, 所以给他去掉
        lis = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li')[:-2]
        # print(lis)
        # 2. 遍历lis, 提取数据
        data_list = []
        for li in lis:
            # 去掉中间那个广告
            if li.get_attribute('class') == 'apartments-pkg apartments':
                # 跳过本次循环, 继续下一次循环
                continue

            # 提取数据
            item = {}
            # 获取租房信息的a标签
            a = li.find_element_by_xpath('./div[2]/h2/a')
            # 获取a标签的文本, 也就是租房信息标题
            item['title'] = a.text
            # 获取a标签的href属性, 也就是租房信息的详情URL
            item['url'] = a.get_attribute('href')
            # 获取价格
            item['price'] = li.find_element_by_xpath('./div[3]/div[2]/b').text
            # print(item)
            data_list.append(item)
        # 获取下一页的a标签
        # print('data_list',data_list)
        next_page = self.driver.find_elements_by_class_name("next")
        next_page = next_page[0] if len(next_page) != 0 else None
        print('next_page',next_page)
        return data_list, next_page

    def save_data(self, data_list):
        """保存数据"""
        with open('./test/58租房.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 3. 使用driver对象, 加载起始URL
        self.driver.get(self.url)

        while True:
            # 4. 使用driver对象, 提取数据
            data_list, next_page = self.get_data()
            # 5. 保存数据
            self.save_data(data_list)
            if next_page:
                # 点击下一页的a标签
                next_page.click()
                # 点击完下一页之后, 页面需要加载
                time.sleep(3)
            else:
                break

        # time.sleep(10)
        # 退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    zfs = ZuFangSpider()
    zfs.run()