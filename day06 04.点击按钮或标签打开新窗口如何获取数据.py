from selenium import webdriver
import time

"""
点击按钮或标签打开新窗口
获取新的数据
"""

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')


driver.find_element_by_id('kw').send_keys('jd')
driver.find_element_by_id('su').click()

# 等待页面的加载
time.sleep(2)

driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()

# 等待页面的加载
time.sleep(3)

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.quit()