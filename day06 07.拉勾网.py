from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from chajian.chaojiying import chaojiying

"""
思路:
创建浏览器驱动对象
加载登录页面
等待页面加载完毕
切换到用户名和密码登录模式
输入手机号, 注意此处需要等待并获取输入框
输入密码
点击验证按钮
获取弹出验证图片
使用超级鹰识别图形的坐标
获取到坐标信息, x,y坐标分别除以2; 由于电脑分辨率太过了, 是原来的两倍, 如果是普通分辨率可以除以2,直接用就可以了.
把鼠标移动到, 坐标点的位置进行点击
点击登录按钮
"""

# 创建浏览器驱动对象
driver = webdriver.Chrome()

# 加载登录页面
driver.get('http://www.zhaopingou.com/signin')

# 等待页面加载完毕
time.sleep(2)

# 切换到账号密码登录
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li[2]').click()

# # 显示等待方式
wait = WebDriverWait(driver, 20, 0.5)
# # 等待并获取用户名输入框,显示等待用户名的元素出来为止
# login_name = wait.until(EC.visibility_of_element_located((By.ID,'pwd_login_phone')))
# login_name.send_keys('18665625762')

# 隐式等待方式
driver.implicitly_wait(1)
# 登录名
login_name = driver.find_element_by_xpath('//*[@id="pwd_login_phone"]')
login_name.send_keys('18665625762')
# 密码
password = driver.find_element_by_xpath('//*[@id="form_login_password"]')
password.send_keys('qq292605957')
# 验证码,获取要点击的元素
captcha = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//div[@class="phone_login_pwd"]//iframe[starts-with(@id, "captcha_widget")]'))).click()
# 等待并获取弹出层的元素
captcha_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//iframe[starts-with(@id, "captcha_frame")]')))
# captcha_element.screenshot('a.png')  # 把元素保存为本地的图片(测试使用)
captcha_img = captcha_element.screenshot_as_png

# 使用超级鹰识别图片
result = chaojiying.post_pic(captcha_img, '9101')  # 9101超级鹰解码的类别:http://www.chaojiying.com/price.html
print('result', result)
x_str, y_str = result['pic_str'].split(',')
print('x_str', x_str)
print('y_str', y_str)
x = int(x_str)
y = int(y_str)

# 控制鼠标移动到元素
ActionChains(driver).move_to_element_with_offset(captcha_element, x, y).click().perform()
print(ActionChains(driver).move_to_element_with_offset(captcha_element, x, y).click().perform())
time.sleep(1)

driver.find_element_by_id('free_login_btn').click()



