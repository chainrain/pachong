from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 定位元素的方法
input = driver.find_element_by_id('kw')  # 精确查找,查不到就报错
# print(input)

# 用于获取元素中属性
# print(input.get_attribute('name'))

# 获取标签名
# print(input.tag_name)

# 也支持xpath:find_elements_by_xpath搜索所有,find_element_by_xpath搜索一个
# find_elements_by_xpath （返回一个列表,如果没有就返回一个空列表）
# a_s = driver.find_elements_by_xpath('//*[@id="u1"]/a')
# print(a_s)

# 文本信息
# for a in a_s:
#     print(a.text)

# 搜索名为新闻的对象
xinwen = driver.find_element_by_link_text('新闻')
# 新闻对象
# print(xinwen)
# 新闻链接
# print(xinwen.get_attribute('href'))

# 搜索名局部为hao的对象
hao123 = driver.find_element_by_partial_link_text('hao')
# hao123对象
print(hao123)
# hao123链接
print(hao123.get_attribute('href'))

# 搜索所有名为mnav的class
a_s = driver.find_elements_by_class_name('mnav')
for a in a_s:
    # print(a.get_attribute('class'))
    print(a.get_attribute('href'))
    print(a.text)

# 通过css定位
xinwen = driver.find_element_by_css_selector('#u1 > a:nth-child(1)')
print(xinwen.text)

driver.quit()