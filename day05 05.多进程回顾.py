from  multiprocessing import Process
import time

"""
默认: 主进程结束了, 子进程会继续运行
如果希望主进行结束, 子进程也跟着结束, 此时需要把子进程设置守护进程
"""


def task(msg):
    for i in range(10):
        print(msg)


p1 = Process(target=task, args=('任务1',))
p1.daemon = True
p1.start()

p2 = Process(target=task, args=('任务2',))
p2.daemon = True
p2.start()

print('主进程结束了')

time.sleep(2)



