"""
请求模块:用于封装一个请求数据
"""

class Request(object):
    def __init__(self,url,method='GET',params={},data={},headers={}):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.headers = headers