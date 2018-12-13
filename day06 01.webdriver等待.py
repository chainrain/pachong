from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

"""
之前的话是time.sleep等待,
    这个方法会有个问题,如果等待时间元素还没被加载加载到,有可能no such element找不到元素
所以就会用到另外一些等待方法,
"""

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('itcast')

driver.find_element_by_id('su').click()


# 1.强制等待,timesleep.如果在等待时间内找不到元素,会报错
# time.sleep(0.2)

# 2.隐式等待: 使用driver.implicitly_wait(10), 等待页面完全加载或超时(注意,这个方法里面的值不能过小,如果是0.1一样页不行,)
# driver.implicitly_wait(10)  # 10表示最多10秒来加载页面

# 显示等待: 可以等待某个条件成立为止
wait = WebDriverWait(driver,20,0.5)  # 检查条件的频率, 单位s
next_page = wait.until(EC.presence_of_element_located((By.LINK_TEXT,'下一页>')))

# next_page = driver.find_element_by_link_text('下一页>')

next_page.click()

time.sleep(2)
driver.quit()