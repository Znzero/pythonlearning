# -*- coding:utf-8 -*-
"""
Python 3.9
作者：zengn
日期：2023年01月10日
"""
from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print("{} is producing {} to the queue!".format(self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print("{} is consuming {} in the queue.".format(self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())


def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')


if __name__ == '__main__':
    main()
    """
    队列queue的put方法可以将一个对象obj放入队列中。如果队列已满，此方法将阻塞至队列有空间可用为止。
    queue的get方法一次返回队列中的一个成员。如果队列为空，此方法将阻塞至队列中有成员可用为止。
    queue同时还自带emtpy(), full()等方法来判断一个队列是否为空或已满，但是这些方法并不可靠，
    因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。
    """