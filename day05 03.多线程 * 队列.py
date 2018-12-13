from queue import Queue
from threading import Thread
import time

queue = Queue()


def put():
    for i in range(10):
        print('添加元素: {}'.format(i))
        queue.put(i)


def get():
    while True:
        time.sleep(0.2)
        print('获取元素: {}'.format(queue.get()))
        queue.task_done()


t1 = Thread(target=put)
t1.setDaemon(True)
t1.start()

t2 = Thread(target=get)
t2.setDaemon(True)
t2.start()

queue.join()