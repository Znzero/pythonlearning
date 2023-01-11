# -*- coding:utf-8 -*-
"""
Python 3.9
作者：zengn
日期：2023年01月10日
"""
import threading
import time

def long_time_task(i):
    print('当前子线程: {} - 任务{}'.format(threading.current_thread().name, i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    t1 = threading.Thread(target=long_time_task, args=(1,))
    t2 = threading.Thread(target=long_time_task, args=(2,))
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()

    end = time.time()
    print("总共用时{}秒".format((end - start)))
    """
    主线程根本没有等子线程完成，而是自己结束后就打印了消耗时间。主线程结束后，子线程仍在独立运行
    如果要实现主线程和子线程的同步，我们必需使用join方法
    """