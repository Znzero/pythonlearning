# -*- coding:utf-8 -*-
"""
Python 3.9
作者：zengn
日期：2023年01月10日
"""

from multiprocessing import Process
import os
import time

"""
新创建的进程与进程的切换都是要耗资源的，所以平时工作中进程数不能开太大。
同时可以运行的进程数一般受制于CPU的核数。
除了使用Process方法，我们还可以使用Pool类创建多进程。
"""

def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))  # 使用os.getpid()打印出当前进程的名字。
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task, args=(1,))  # Process()方法接收两个参数, 第一个是target，一般指向函数名，第二个是args，需要向函数传递的参数。
    p2 = Process(target=long_time_task, args=(2,))
    print('等待所有子进程完成。')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))