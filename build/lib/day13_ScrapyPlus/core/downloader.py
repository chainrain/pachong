"""
下载器模块:发送请求,获取响应数据
"""
import requests
from ..http.response import Response

class Downloader(object):
    def get_response(self,request):
        """根据请求,获取响应数据"""

        # 如果是GET请求,发送GET请求获取数据
        if request.method.upper() == 'GET':
            resp = requests.get(request.url,params=request.params,headers=request.headers)
        elif request.method.upper == 'POST':
            resp = requests.post(request.url,data=request.data,headers=request.headers)
        else:
            raise Exception('暂时只支持GET和POST请求')

        # 为了让代码有更好的可扩展性,需要我们自定义响应对象,对requests中响应到对象进行封装
        return Response(resp.url,status_code=resp.status_code,headers=resp.headers,body=resp.content)