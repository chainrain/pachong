from multiprocessing.dummy import Pool
import time
from queue import Queue

"""
注意,这里使用了的是multiprocessing.dummy下面的pool,
             不是multiprocessing下面的pool
"""

queue = Queue()


def add():
    for i in range(10):
        print('添加元素: {}'.format(i))
        queue.put(i)


def get():
    while True:
        time.sleep(0.2)
        print('获取元素: {}'.format(queue.get()))
        queue.task_done()


pool = Pool(5)  # 指定线程池中线程的个数

# 实现线程池, 执行异步任务
# 在使用线程池执行异步任务时候, 线程默认都是守护线程
pool.apply_async(add)
pool.apply_async(get)

# 测试添加睡眠时间,不然get的速度太快了,完成之后程序就停了
time.sleep(0.1)
# 关闭线程池, 不能再给线程分配新任务了
pool.close()
# 让主线程, 等待子线程完成
queue.join()
