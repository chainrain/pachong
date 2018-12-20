"""
请求模块:用于封装一个请求数据
"""

class Request(object):
    def __init__(self,url,method='GET',params={},data={},headers={},callback=None,meta={}):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.headers = headers

        self.callback = callback  # 新增回调函数
        self.meta = meta  # 新增数据传递函数