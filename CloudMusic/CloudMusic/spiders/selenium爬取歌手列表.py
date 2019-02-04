from selenium import webdriver

# 创建设置对象
options = webdriver.ChromeOptions()
# 更换头部, 注意此处的user-agent必须是小写, 否则不生效
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')

driver = webdriver.Chrome(options=options)

driver.get('https://music.163.com/#/discover/artist/signed/')

page = driver.page_source

print(page)