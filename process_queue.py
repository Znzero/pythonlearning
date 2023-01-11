# -*- coding:utf-8 -*-
"""
Python 3.9
作者：zengn
日期：2023年01月10日
"""

"""
仅适用于两个进程通过Queue()进行通信。
如果要实现多个进程进行数据交换呢（比如1个父进程和2个子进程需要共享内存)，这是需要使用Manager()方法提供的Queue()。
from multiprocessing import Manager
q = Manager().Queue()
否则会出现RuntimeError: Queue objects should only be shared between processes through inheritance的报错
"""

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: {}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read:{}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()