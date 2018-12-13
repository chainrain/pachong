import time
from selenium import webdriver
from io import BytesIO
from PIL import Image
import pytesseract

"""
有些网站的数据是采用了反爬手段,
例如:猫眼电影,http://maoyan.com/films/1208282里面,票房,评分类的数据
这里就要采用其他方案:保存数据为图片->pytesseract识别

注意,有时候会数据对不上,那么就用加大图片的方法
"""


def image_to_string(png):
    """3
    识别图片内容, 获取文本字符串
    :param img: 图片二进制数据
    :return: 文本字符串
    """
    # 把二进制图片转换为Image对象
    image = Image.open(BytesIO(png))

    # 修改图片的大小为原来的两倍
    im = image.resize((int(image.width * 2), int(image.height * 2)))
    # im = im.convert('L')
    # image.save('a.png')
    # im = im.point(lambda x: 0 if x < 120 else 255)
    # 使用tensoract识别图片内容
    # image: 要识别的图片
    # config="-psm 7" : 配置图片按一行文本进行识别
    # lang: 识别的语言是中文+英文
    result = pytesseract.image_to_string(im, config="-psm 7", lang='eng+chi_sim')
    # 返回识别后结果
    return result



driver = webdriver.Chrome()
driver.get('http://maoyan.com/films/1225632')


item = {}

# 评分
score = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/span/span')
item['评分'] = image_to_string(score.screenshot_as_png)  # score.screenshot_as_png  保存二进制分数图片
score.screenshot('评分.png')

# 评论
comments = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div/span/span')
item['评论'] = image_to_string(comments.screenshot_as_png) + '万'  # comments.screenshot_as_png  保存二进制评论图片
comments.screenshot('评论.png')

# 票房
income = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[2]/div')
item['票房'] = image_to_string(income.screenshot_as_png)  # income.screenshot_as_png  保存二进制票房二进制图片
income.screenshot('票房.png')

# score.screenshot('./test/评分图片.png')
# comments.screenshot('./test/评论图片.png')
# income.screenshot('./test/票房图片.png')
print(item)
driver.quit()
