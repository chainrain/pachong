"""
下载器中间件: 在引擎和下载器之间,用于处理请求和响应的
"""


class DownloaderMiddleware1(object):
    def process_request(self, request):
        """
        处理请求
        :param request: 请求对象
        :return:
        """
        print('DownloaderMiddleware1-process_request_{}'.format(request.url))
        return request

    def process_response(self,response):
        """
        处理响应
        :param response: 响应对象
        :return:
        """
        print('DownloaderMiddleware1-process_response_{}'.format(response.url))
        return response

class DownloaderMiddleware2(object):
    def process_request(self, request):
        """
        处理请求
        :param request: 请求对象
        :return:
        """
        print('DownloaderMiddleware2-process_request_{}'.format(request.url))
        return request

    def process_response(self,response):
        """
        处理响应
        :param response: 响应对象
        :return:
        """
        print('DownloaderMiddleware2-process_response_{}'.format(response.url))
        return response