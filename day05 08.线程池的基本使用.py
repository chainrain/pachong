from multiprocessing.dummy import Pool

import time

"""
注意,这里使用了的是multiprocessing.dummy下面的pool,
             不是multiprocessing下面的pool
"""

# pool = Pool()  # 默认为CPU个数
pool = Pool(5)  # 指定线程池中线程的个数


def task(msg):
    for i in range(10):
        time.sleep(0.2)
        print(msg)



# 让线程池调度任务
# apply: 同步执行任务: 前面不结束, 后面就不执行
# pool.apply(task, args=('任务1', ))
# pool.apply(task, args=('任务2', ))

# 实现线程池, 执行异步任务
# 在使用线程池执行异步任务时候, 线程默认都是守护线程
pool.apply_async(task,args=('任务1',))
pool.apply_async(task,args=('任务2',))


# 关闭线程池, 不能再给线程分配新任务了
pool.close()
# 让主线程, 等待子线程完成
pool.join()
