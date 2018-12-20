from queue import Queue

queue = Queue(maxsize=3)

# 添加元素
queue.put('a')
queue.put('b')
queue.put('c')
# queue.put('d')         # 如果maxsize=3,那么这个就put不进来,卡线程
# queue.put_nowait('d')  # 如果maxsize=3,put_nowait这个会报错queue.Full溢出

print(queue.get())
print(queue.get())
print(queue.get())
# print(queue.get())     # 如果maxsize=3,get的数量超过3的话,也会卡线程
# print(queue.get_nowait())  # 如果maxsize=3,put_nowait这个会报错queue.Empty空

# 查看元素数量
print(queue.qsize())
# unfinished_tasks: 没有完成任务数量
print(queue.unfinished_tasks)
# queue.task_done()完成一个任务
queue.task_done()
queue.task_done()
queue.task_done()
print(queue.unfinished_tasks)  # 完成了任务,显示0

# 让当前线程等待, 等待到unfinished_tasks==0的时候为止
queue.join()