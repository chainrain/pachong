import requests



import sys,time
#导入模块

response = requests.get('http://fs.w.kugou.com/201811251846/05c97ed289d0464495dcb910ab3cfa5b/G109/M06/01/11/TZQEAFv4HByAawjVADew_QPXlEU560.mp3')
# print('response.text',response.text)
# print('response.content.decode()',response.content)
# print(response.headers)
# print(len(response.content))
with open('/home/python/Desktop/01.mp3','wb') as f:








    index = f.write(response.content)




"""
# mkdir test
# python@ubuntu:~/Desktop$ cp  ../../../usr/lib/python3.5/*.py test/





import multiprocessing, os, time, random

def copy_file(queue, file_name, source_folder_name, dest_folder_name):
    f_read = open(source_folder_name + "/" + file_name, "rb")
    f_write = open(dest_folder_name + "/" + file_name, 'wb')
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
        f_write.close()
        f_read.close()

        queue.put(file_name)

def main():
    # 拷贝文件主方法
    # 获取要复制的文件夹
    source_folder_name = '/home/python/Desktop/'+input("需要拷贝的文件夹")
    # 整理目标文件夹
    desk_folder_name = source_folder_name + "[附件]"
    # 创建目标文件夹
    try:
        os.mkdir(desk_folder_name)
    except:
        print("文件夹已经存在，创建失败")
        pass
    # 创建Queue
    queue = multiprocessing.Manager().Queue()
    # 创建进程池
    pool = multiprocessing.Pool(3)
    # 获取这个文件夹中所有的普通文件名
    files_name = os.listdir(source_folder_name)
    # 向进程池中添加任务(循环得到的文件名)
    for file_name in files_name:
        pool.apply_async(copy_file, args=(queue, file_name, source_folder_name, desk_folder_name))
    # 主进程显示进度，关闭了池之后
    pool.close()

    all_file_num = len(files_name)
    while True:
        file_name = queue.get()
        if file_name in files_name:
            files_name.remove(file_name)

        copy_rate = (all_file_num - len(files_name)) * 100 / all_file_num
        print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="")
        # print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="")
        if copy_rate >= 100:
            break
    print()
    """