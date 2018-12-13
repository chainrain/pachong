from gevent import monkey  # 首先打补丁
monkey.patch_all()

from queue import Queue
# 导入协程池,结论; 在使用协程池的时候, 必须要打猴子补丁,不然有些功能就不能执行,比如说异步,睡眠等
from gevent.pool import Pool
import time



queue = Queue()


def put():
    for i in range(10):
        print('添加元素: {}'.format(i))
        queue.put(i)


def get():
    while True:
        time.sleep(0.1)
        print('获取元素: {}'.format(queue.get()))
        queue.task_done()


pool = Pool()
pool.apply_async(put)
pool.apply_async(get)
time.sleep(0.1)
queue.join()
