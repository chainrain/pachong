from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.set_headless()

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")