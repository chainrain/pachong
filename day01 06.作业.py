
import requests
import re
class DownloadKugouMusic:
    def __init__(self):
        # 地址栏
        self.url = 'http://www.kugou.com/yy/test/rank.test'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }



    def run(self):
        url_list = self.get_url_list()
        print(url_list)
        print(type(url_list))
        for url in url_list:
            music_detail = requests.get(url,headers=self.headers)
            print(music_detail.content.decode())
            # print(re.findall('src.*',music_detail.content.decode()))


    def get_url_list(self):
        """得到音乐的url地址"""
        html = requests.get(self.url,headers=self.headers)
        html_response = html.content.decode()
        html_response = re.findall('http://www.kugou.com/song/.*.test',html_response)
        return html_response


if __name__ == '__main__':
    dkm = DownloadKugouMusic()
    dkm.run()