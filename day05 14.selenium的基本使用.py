"""
Selenium是一个Web的自动化测试工具,
最初是为网站自动化测试而开发的，
Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器），
可以接收指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏
安装:pip install selenium
"""
from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome()

# 加载页面,注意协议头必须带:httpshttps://
driver.get('https://www.baidu.com/')

# 找到输入框的id,填写内容
# driver.find_element_by_id('kw').send_keys('图拉丁')
# 点击搜索按钮的id,点击
# driver.find_element_by_id('su').click()

# 获取渲染后文本内容
# print(driver.page_source)

# 获取当前URL
# print(driver.current_url)

# 获取cookie信息
print(driver.get_cookies())

# 把get_cookies()获取到字典列表, 转换为'name':'value'这样的字典格式
cookies = {}
for cookie in driver.get_cookies():
    cookies[cookie['name']] = cookie['value']
print(cookies)
# cookies1 = {cookie['name']:cookie['value']  for cookie in driver.get_cookies() }
# print(cookies1)

time.sleep(1)
driver.quit()
