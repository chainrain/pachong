"""
报错重复访问
安装
pip3 install retrying
"""
import requests
from retrying import retry


@retry(stop_max_attempt_number=3)  # ctrl点击retry,进入方法内部可以看到Retrying类,里面有各种方法.注意,这个重复访问的方法,要指定timeout超时,不然回一直卡在第一次
def get_page_from_url(url):
    print('执行了')
    response = requests.get(url=url, timeout=2)
    return response.content.decode()


if __name__ == '__main__':
    html = get_page_from_url('http://www.google.com')
    print(html)
