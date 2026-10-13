#装饰器
"""
@装饰器A
@装饰器B
def 目标函数():
    pass
- 目标函数 = A(B(目标函数))

"""
import time
def A(f):
    def inner():
        print("A执行前：")
        f()
        print("A执行后:")
    return inner

def B(f):
    def inner():
        print("B执行前:")
        f()
        print("B执行后:")
    return inner
@A
@B
def func():
    print("原始func函数内部")
func()

# 写一个功能，统计一个函数运行花了多长时间，但是不改动源代码

# 外层：接收一个函数作为参数
def timer(func):
    # 内层函数：包装原来的函数，增加额外逻辑
    def wrapper():
        start = time.time()
        func() # 执行原来传进来的函数
        end = time.time()
        print(f"耗时：{end - start}")
    return wrapper # 返回内层wrapper函数对象

def work():
    time.sleep(2)
    print("工作完成")
work = timer(work)
work() # 调用包装后的函数
