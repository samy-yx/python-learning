import threading
import time

#方法1
# def work(name):
#     print(f"线程{name}开始干活了")
#     time.sleep(0.5)
#     print(f"线程{name}干完了")
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target = work,args = ("A",))
#     t2 = threading.Thread(target = work,args = ("B",))
#
#     t1.start() # 启动线程
#     t2.start()
#
#     t1.join() # 阻塞主线程
#     t2.join()
#
#     print("所有线程全部完成")

#方法2 ：继承Thread，重写run
# class MyThread(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#        print(f"自定义线程{self.name}启动")
#        time.sleep(0.5)
#        print(f"自定义线程{self.name}结束")
#
# if __name__ == "__main__":
#     t1 = MyThread("1号")
#     t1.start()
#     t1.join()

#方法3：线程池
from concurrent.futures import ThreadPoolExecutor

def task(num):
    print(f"任务{num}开始")
    time.sleep(0.5)
    return f"任务{num}完成"

if __name__ =="__main__":
    with ThreadPoolExecutor(max_workers = 3) as pool:
        futures = [pool.submit(task,i) for i in range(5)]
        for f in futures:
            print(f.result())
    print("线程池自动关闭")