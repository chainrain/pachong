import time

from selenium import webdriver

from chajian.chaojiying import chaojiying

driver = webdriver.Chrome()
# 网站
driver.get('https://www.douban.com/')
# 账号
driver.find_element_by_id('form_email').send_keys('18665625762')
# 密码
driver.find_element_by_id('form_password').send_keys('qq292605957')


# 获取验证码图片
captcha_image = driver.find_element_by_id('captcha_image')
print(captcha_image)
if captcha_image != 0:
    img = captcha_image.screenshot_as_png
    # captcha_image.screenshot('05_douban.png')# 把元素保存一张图片到本地(测试的)
    result = chaojiying.post_pic(img,'1008')
    code = result['pic_str']
    print(code)
    driver.find_element_by_id('captcha_field').send_keys(code)

# 点击登录
driver.find_element_by_class_name('bn-submit').click()

time.sleep(3)
driver.quit()







"""
按find_elements_by_id('captcha_image')找

from selenium import webdriver
import time
# 导入超级鹰
from chaojiying import chaojiying


driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

# 输入账号
driver.find_element_by_id('form_email').send_keys('583349285@qq.com')
# 输入密码
driver.find_element_by_id('form_password').send_keys('ivanlee1986')

# 获取验证码图片的元素
captcha_images = driver.find_elements_by_id('captcha_image')  # 列表
if len(captcha_images) != 0:  # 列表判断非空
    # 验证码图片元素
    captcha_image = captcha_images[0]  # 拿列表的第一个

    # 把元素保存一张图片到本地(测试的)
    captcha_image.screenshot('05_douban.png')
    # 把验证码图片元素转换为二进制数据(页面中任何元素都可以转图片)
    img = captcha_image.screenshot_as_png
    # 返回值是一个字典
    result = chaojiying.post_pic(img, '1008')
    # 获取验证码
    code = result['pic_str']
    # 输入验证码
    driver.find_element_by_id('captcha_field').send_keys(code)

# 点击登录按钮
driver.find_element_by_class_name('bn-submit').click()

time.sleep(10)
driver.quit()
"""