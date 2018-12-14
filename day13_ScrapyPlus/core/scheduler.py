"""
调度器模块

步骤:
1.初始一个队列,用于缓存请求
2.提供添加请求的方法
3.提起获取请求的方法
4.请求去重的方法


"""
# from queue import Queue  # 如果要做到兼容py2,py3,就要换一下,用six的(如果没有,pip install six)
from six.moves.queue import Queue  # 报红没关系


class Scheduler(object):
    def __init__(self):
        """初始化队列,缓存请求"""
        self.queue = Queue()

    def add_request(self, request):
        """提供添加请求的方法"""
        self.queue.put(request)

    def get_request(self):
        """提起获取请求的方法"""
        request = self.queue.get()
        return request
    def request_seen(self,request):
        """请求去重的方法"""
        # todo
        pass