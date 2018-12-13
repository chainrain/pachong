from threading import Thread


def task(msg):
    for i in range(10):
        print(msg)

t1 = Thread(target=task,args=('任务1',))
t1.setDaemon(True)
t1.start()
t2 = Thread(target=task,args=('任务2',))
t2.setDaemon(True)
t2.start()

print('主线程执行完毕')
"""
注意!!
默认情况下, 线程都不是守护线程, 主线程结束了, 子线程继续跑, 直到其执行完毕为止
守护线程: 当主线结束了, 守护线程会自动结束.xx.setDaemon(True)
"""



