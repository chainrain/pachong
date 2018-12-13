"""
响应模块:用于封装一个响应数据
"""
class Response(object):
    def __init__(self,url,status_code,headers={},body=None):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body