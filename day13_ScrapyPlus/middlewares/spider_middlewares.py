"""
爬虫中间件: 在引擎和爬虫中间,用于处理请求和响应数据的
"""


class SpiderMiddleware(object):
    def process_request(self, request):
        """
        处理请求
        :param request: 请求对象
        :return:
        """
        print('SpiderMiddleware-process_request_{}'.format(request.url))
        return request

    def process_response(self, response):
        """
        处理响应
        :param response: 响应对象
        :return:
        """
        print('SpiderMiddleware-process_request_{}'.format(response.url))
        return response