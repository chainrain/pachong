from multiprocessing import Process, JoinableQueue
import time

queue = JoinableQueue()


def put():
    for i in range(10):
        print('添加元素: {}'.format(i))
        queue.put(i)

def get():
    while True:
        time.sleep(0.1)
        print('获取元素: {}'.format(queue.get()))
        queue.task_done()

p1 = Process(target=put)
p1.daemon = True
p1.start()

p2 = Process(target=get)
p2.daemon = True
p2.start()

time.sleep(0.5)  # 由于进程启动比较慢, 所以导致字进程任务还没有执行, 就来到这里了, 程序就提前结束了,解决方案: 稍微等待
queue.join()  # 让主进程等待队列任务完成