from selenium import webdriver
"""
Chrome的无头模式(headless)
什么是无头模式(headless)
就没有渲染界面
为什么要使用无头模式:
可以降低对GPU的消耗, 提高执行效率
怎么启用Chrome无头模式

创建ChromeOptions对象
ChromeOptions对象设置无界面
在创建Chrome驱动的时候, 把ChromeOptions对象 传入
"""

options = webdriver.ChromeOptions()
options.headless = True

options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"')
# 3. 能够给Chrome设置代理IP
# options.add_argument('--proxy-server=http://58.53.128.83:3128')

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com/')
# print(driver.page_source)
# 快照
driver.save_screenshot('baidu.png')
print(driver.page_source)

driver.quit()