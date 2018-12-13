from selenium import webdriver
import time

"""
处理需要n内嵌网页登录的情况
例子:登录QQ邮箱,使用了iframe表单页面
"""

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')

# 由于登录页面在iframe, 每一个iframe独立页面, 只有把driver切入到iframe中, 才能获取iframe中内容
driver.switch_to.frame('login_frame')
"""
driver.switch_to.frame('frame_name') # 根据frame名称切换
driver.switch_to.frame(1)  # 根据索引切换
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0]) # 根据元素进行切换
"""

# 输入账号
driver.find_element_by_id('u').send_keys('905531354')
# 输入密码
driver.find_element_by_id('p').send_keys('zhouxingyu')
# 点击登录按钮
driver.find_element_by_id('login_button').click()

time.sleep(10)
driver.quit()