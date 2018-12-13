# 打猴子补丁(热补丁) : 可以自动在等待, IO操作, 网络等位置自动添加协程间切换代码
from gevent import monkey
monkey.patch_all()

# 导入协程池,结论; 在使用协程池的时候, 必须要打猴子补丁,不然有些功能就不能执行,比如说异步,睡眠等
from gevent.pool import Pool
import time


def task(msg):
    for i in range(10):
        time.sleep(0.1)
        print(msg)

pool = Pool()

#  使用协程池执行同步任务
# pool.apply(task, args=('任务1', ))
# pool.apply(task, args=('任务2', ))

pool.apply_async(task,args=('任务1',))
pool.apply_async(task,args=('任务2',))

pool.join()