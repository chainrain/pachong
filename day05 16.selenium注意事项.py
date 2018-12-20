from selenium import webdriver

# 创建驱动对象
driver = webdriver.Chrome()
# 加载页面
driver.get('https://www.baidu.com/')


# 1. find_element 和find_elements的区别：
# find_element: 返回找到第一个元素,如果没有报错
# a = driver.find_element_by_xpath('//*[@id="u1"]/a')
# print(a.text)
# find_elements: 返回找到的所有元素列表, 如果没有找到返回空列表
# a = driver.find_elements_by_xpath('//*[@id="u1"]/a')
# print(a)
#
# 1. by_link_text和by_partial_link_text的区别：


# # by_link_text: 全部文本都一样
# hao123 = driver.find_element_by_link_text('hao123')
# hao123 = driver.find_element_by_link_text('hao')
# print(hao123.text)
# # by_partial_link_text: 包含某个文本
hao123 = driver.find_element_by_partial_link_text('hao')
print(hao123.text)
# 3. by_xpath只能获取元素, 要获取属性和文本需要使用get_attribute(属性名) 和.text
# text =  driver.find_element_by_xpath('//*[@id="u1"]/a[1]/text()') # 错误
# text =  driver.find_element_by_xpath('//*[@id="u1"]/a[1]/@href') # 错误
a = driver.find_element_by_xpath('//*[@id="u1"]/a[1]')
# 获取文本
print(a.text)
print(a.get_attribute('href'))

driver.quit()
