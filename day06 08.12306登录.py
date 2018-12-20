from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from chajian.chaojiying import chaojiying
from PIL import Image

"""
实现12306的登录
12306是用
"""


def size(img_bytes):
    """
    :param img_bytes: 原来图片二进制数据
    :return:
    """
    # 把图片二进制数据,转换Image对象
    im = Image.open(BytesIO(img_bytes))

    # 创建bytesIO对象, 用于缓存图片
    bytes_io = BytesIO()
    # 把图片保存在bytes_io
    im.save(bytes_io, format='png')
    # 从bytes_io中获取图片的二进制数据
    return bytes_io.getvalue()


driver = webdriver.Chrome()

driver.get('https://kyfw.12306.cn/otn/resources/login.html')

time.sleep(1)

# 切换为账号登录
driver.find_element_by_class_name('login-hd-account').click()

# 账号
driver.find_element_by_id('J-userName').send_keys('18665625762')

# 密码
driver.find_element_by_id('J-password').send_keys('qq292605957')

time.sleep(1)

# 获取验证码图片
ima_element = driver.find_element_by_id('J-loginImg')
img_bytes = ima_element.screenshot_as_png

# 自定义函数
img_bytes = size(img_bytes)

# 使用超级鹰9004解码
result = chaojiying.post_pic(img_bytes, '9004')
print('result',result)

# 获取每一个点击位置
groups = result['pic_str'].split('|')
print('groups', groups)
# 对于每一个位置使用分割,组成一个列表
positions = [[int(number) for number in group.split(',')] for group in groups]
print('positions', positions)

for position in positions:
    # 点击图片
    ActionChains(driver).move_to_element_with_offset(ima_element, position[0], position[1]).click().perform()
    time.sleep(1)

# 登录
driver.find_element_by_link_text('立即登录').click()
