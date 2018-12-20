from selenium import webdriver
import json
import time


class DouyuSpider(object):
    """爬取斗鱼房间的信息"""
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.get('https://www.douyu.com/directory/all')
        while True:
            data_list = self.get_data_list()
            self.save_data(data_list)
            next_page = self.next_page_button()
            if next_page:
                next_page.click()
                time.sleep(3)
            else:
                break
        self.driver.quit()

    def get_data_list(self):
        """从当前页面拿到房间的LI标签列表"""
        # 所有房间的li
        lis = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')
        data_list = []  # 用来存储一个页面的房间详情,一共大概120个
        for li in lis:
            item = {}  # 单个房间的详情
            item['房间图片'] = li.find_element_by_xpath('./a/span/img').get_attribute('data-original')
            item['房间名称'] = li.find_element_by_xpath('./a/div/div/h3').text
            item['房间类别'] = li.find_element_by_xpath('./a/div/div/span').text
            item['房间所有者'] = li.find_element_by_xpath('./a/div/p/span[1]').text
            item['房间热度'] = li.find_element_by_xpath('./a/div/p/span[2]').text
            data_list.append(item)
        return data_list

    def next_page_button(self):
        """拿到是否有下一页的按钮"""
        next_page = self.driver.find_element_by_link_text('下一页')
        # 如果在a标签的class中有disable,就说明没有下一页
        next_class = next_page.get_attribute('class')
        if next_class.find('disable') != -1:  # 等于负1,相当于找不到.不等于负1,相当于找到
            next_page = None
        print(next_page.get_attribute('href'))
        return next_page

    def save_data(self, data_list):
        """保存数据"""
        with open('./test/斗鱼热门房间.jsonlines','a',encoding='utf8') as f:
            for data in data_list:
                json.dump(data,f,ensure_ascii=False)
                f.write('\n')
if __name__ == '__main__':
    spider = DouyuSpider()
    spider.run()
