#自定义Process子类创建进程
""""
 multiprocessing.Process是进程基类，自定义子类需要继承Process，并且重写run()方法

 - run：进程启动后自动执行的业务逻辑
 - start():必须调用，会自动创建子进程，调用run()，不能直接调用run()
 - os.getpid():获取当前进程id，os.getppid()：获取父进程id
"""

import os
import time
import random
from multiprocessing import Process,Queue
#
# #自定义进程类，继承Process
# class worker(Process):
#     def run(self):
#         #子进程执行逻辑
#         print(f"子进程id:{os.getpid()},父进程id:{os.getppid()}")
#
# if __name__ == "__main__":
#     print(f"主进程id:{os.getpid()}")
#     #创建3个子进程
#     for i in range(3):
#         p = worker()
#         p.start() # 启动进程，自动调用run()
#         p.join()#阻塞主进程，等待当前子进程执行完毕


#进程池
"""
当需要大量子进程时，频繁创建销毁进程开销大，用进程池预先创建一批进程，重复使用

- multiprocessing.Pool(processes = N) 创建容量为N的进程池
- apply(func):同步阻塞，任务排队，一个执行完才执行下一个
- apply_async(func)：异步非阻塞，任务并发提交(常用)
- close():不再接收新任务
- join:阻塞主进程，等池中所有任务完成，close必须在join前
"""

# def func():
#     #任务：打印10次进程id
#     for i in range(10):
#         print(f"进程：{os.getpid()}，{i}")
#         time.sleep(0.2)
#
# if __name__ == "__main__":
#     process_num = 3
#     pool = multiprocessing.Pool(process_num)
#
#     #提交三个任务到进程池
#     for i in range(4):
#         #pool.apply(func) # 阻塞式
#         pool.apply_async(func) # 非阻塞式
#     pool.close()
#     pool.join()
#     print("全部任务结束")


#进程间通信
"""
多进程之间内存相互隔离，全局变量/普通列表不能共享
- Queue:队列通信
    - multiprocessing.Queue:是进程安全的先进先出队列，用来在独立进程之间传递数据
    - put():往队列里放数据
    - get():从队列里取数据，没有数据时阻塞等待
"""
#生产者——消费者模型

#生产者：放数据
def producer(q:Queue):
    for _ in range(5):
        num = random.randint(1,20)
        q.put(num)
        print(f"生产者{os.getpid()}放入:{num}")
        time.sleep(0.3)
    #生产全部完成，放入结束信号
    q.put(None)

#消费者：取数据
def consumer(q:Queue):
    while True:
        data = q.get()
        print(f"消费者{os.getpid()}取出：{data}")
        time.sleep(0.5)
        #队列为空，退出循环
        if data == None:
            break

if __name__ =="__main__":
    q = Queue()
    p1 = Process(target = producer,args = (q,))
    p2 = Process(target = consumer,args = (q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主程序结束")














