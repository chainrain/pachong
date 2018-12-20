"""
调度器模块

步骤:
1.初始一个队列,用于缓存请求
2.提供添加请求的方法
3.提起获取请求的方法
4.请求去重的方法


"""
# from queue import Queue  # 如果要做到兼容py2,py3,就要换一下,用six的(如果没有,pip install six)
import hashlib

import six
from six.moves.queue import Queue  # 报红没关系
from w3lib.url import canonicalize_url  # w3lib 是第三方模块
from ..utils.log import logger


class Scheduler(object):
    def __init__(self):
        """初始化队列,缓存请求"""
        self.queue = Queue()
        self.total_request_num = 0
        # 2. 在init方法中, 创建set集合, 用于存储请求的指纹字符串(去重容器)
        self.filter_container = set()
        # 3. 定义变量, 用于统计过滤掉请求数量
        self.filter_request_num = 0

    def add_request(self, request):
        """提供添加请求的方法"""
        # 如果这个请求重复了, 就直接过滤掉
        if self.request_seen(request):
            logger.info('被过滤请求: {}'.format(request.url))
            self.filter_request_num += 1
            return

        self.queue.put(request)
        # 2. 在add_request方法中, 每添加一个请求, 总请求数量增加1
        self.total_request_num += 1

    def get_request(self):
        """提起获取请求的方法"""
        request = self.queue.get()
        return request

    def request_seen(self,request):
        """请求去重的方法"""
        # todo
        """
        请求去重的方法
        :param request:
        :return: 如果返回True , 说明该请求重复了, 否则说明该请求是新的请求
        """
        # 1. 根据请求生成要给指纹字符串
        # 2. 在init方法中, 创建set集合, 用于存储请求的指纹字符串(去重容器)
        fp = self.gen_fp(request)
        # 3. 如果去重容器中, 已经有这个指纹了, 说明这个请求重复了, 返回True
        if fp in self.filter_container:
            return True

        # 4. 如果来到这里, 说明新请求
        # 4.1 把请求添加到去重容器中
        self.filter_container.add(fp)
        # 5. 返回False
        return False



        # 增加生成请求指纹的方法

    def gen_fp(self, request):
        """
        根据请求, 生成该请求对应指纹字符串
        :param request: 请求对象
        :return:  指纹
        """
        # 1. 对请求的URL进行规范化处理
        url = canonicalize_url(request.url)
        # 2. 把请求方法名转转换大写
        method = request.method.upper()
        # 3. 请求params参数进行排序
        params = sorted(request.params, key=lambda x: x[0])
        # 4. 对data参数进行排序
        data = sorted(request.data, key=lambda x: x[0])
        # 5. 使用sha1算法, 对上面的数据进行处理, 生成一个指纹字符串
        # 5.1 获取sha1算法对象
        sha1 = hashlib.sha1()
        # 5.2 向sha1算法中添加数据
        sha1.update(self.str_to_bytes(url))
        sha1.update(self.str_to_bytes(method))
        sha1.update(self.str_to_bytes(str(params)))
        sha1.update(self.str_to_bytes(str(data)))
        # 5.3 生成指纹字符串
        return sha1.hexdigest()

    def str_to_bytes(self, s):
        if six.PY3:
            # 如果是py3
            return s.encode('utf-8') if isinstance(s, str) else s
        else:
            # 不是py3, 就是py2
            return s if isinstance(s, str) else s.encode('utf-8')
