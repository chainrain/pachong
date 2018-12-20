from selenium import webdriver
"""
Phantomjs就是要给无界面浏览器
pip install Phantomjs
"""

# 1. 设置请求头, 是字典
desired_capabilities = {
    'phantomjs.page.settings.userAgent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
}

# 2. 给PhantomJs设置代理, 是列表
service_args = [
    '--proxy=http://58.53.128.83:3128'
]

driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities,service_args=service_args)

driver.get('https://www.baidu.com/')

# 保存快照
driver.save_screenshot('./test/baidu.png')

driver.quit()