from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import json


class ZuFangSpider(object):
    def __init__(self):
        #  1. 准备起始URL
        self.url = 'https://www.qiushibaike.com/'
        #  7. 实现无界面的浏览器
        options = Options()
        options.headless = True
        #  2. 创建driver对象
        self.driver = webdriver.Chrome(options=options)

    def get_data(self):
        """提取数据, 返回数据列表"""
        # 我们也是使用XPATH语法提取数据, 使用原则都是一样的
        # 1. 先分组, 获取包含所有租房信息的li标签列表
        lis = self.driver.find_elements_by_xpath('//*[@id="content-left"]/div')
        # print(lis)
        # 2. 遍历lis, 提取数据
        data_list = []
        for li in lis:
            item = {}
            a = li.find_element_by_xpath('./a/div/span')
            item['内容'] = a.text
            smile = li.find_element_by_class_name('stats-vote')
            item['好笑数'] = smile.text
            comment = li.find_element_by_class_name('stats-comments')
            item['评论数'] = comment.text
            # 好评论
            try:
                good_comment_name = li.find_element_by_class_name('cmt-name')
                good_comment_detail = li.find_element_by_class_name('main-text')
                item['好评人: ' + good_comment_name.text] = good_comment_detail.text
            except:
                pass
            data_list.append(item)
            print(item)

        # # 获取下一页的a标签
        # next_page = self.driver.find_element_by_link_text("下一页")
        # next_page = next_page if len(next_page.text) != 0 else None
        # print('next_page', next_page)
        # print(self.driver.find_element_by_class_name('next').text)

        next_page = self.driver.find_element_by_class_name("next")
        next_page = next_page if self.driver.find_element_by_class_name('next').text != '更多' else None
        print(self.driver.find_element_by_class_name('next').text)

        return data_list, next_page

    def save_data(self, data_list):
        """保存数据"""
        with open('./test/糗事热门.jsonlines', 'a', encoding='utf8') as f:
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
                time.sleep(0.2)
            else:
                break

        # time.sleep(10)
        # 退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    zfs = ZuFangSpider()
    zfs.run()
