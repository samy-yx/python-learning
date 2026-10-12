#装饰器
#装饰器"包装套路"本质就是闭包
"""
闭包三个条件：
- 1.外部函数里定义了内部函数
- 2.内部函数用到了外部函数的变量
- 3.外部函数把内部函数作为返回值
"""
# 用闭包手搓原始装饰器
from math import sqrt

#原始函数：求平方根
# def func(x):
#     return sqrt(x)
#
# #装饰器：给函数"加绝对值"的能力，不修改func
# def decorator(f): # 外部函数，参数是一个函数
#     def inner(x): # 内部函数：用到了外部参数 f
#         x = abs(x) # 新加的功能，先取绝对值
#         return f(x) # 再调用原函数
#     return inner # 再返回内部函数

# 手动装饰：把func换成"装饰后的版本"
# func = decorator(func)
# print(func(-4))
#________________________________________________________________________________
# 手动写func = decorator(func)太啰嗦，Python 提供了 `@` 语法糖，效果完全等价
def decorator(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

@decorator # 等价于 func = decorator(func)
def func(x):
    return sqrt(x)

print(func(-9))
print(func.__name__)

# 参数传递： *arg,**kwargs
import time

def timer(func):
    def wrapper(*args,**kwargs):#借助任意位置参数和关键字参数
        start = time.perf_counter()
        result = func(*args,**kwargs) # 原样转发给原函数
        print(f"[{func.__name__}] 耗时 {time.perf_counter() - start:.4f}秒")
        return result
    return wrapper

# 3.用同一个装饰器装饰"参数完全不同的"两个函数
@timer
def add(x,y):
    time.sleep(0.1)
    return x + y

@timer
def greet(name,msg = "你好"):
    time.sleep(0.5)
    return f"{msg},{name}!"

print(add(3,5))
print(greet("张三",msg = "欢迎"))

# 4.多层装饰器 洋葱模型
"""
多个装饰器叠加时，装饰阶段从里到外(离函数最近的先装饰)。调用阶段从外到里(最外层的先执行前后处理)
"""
def decotator_a(func):
    def wrapper(*args,**kwargs):
        print("A 前处理：进入外层")
        result = func(*args,**kwargs)
        print("A 后处理：离开外层")
        return result
    return wrapper

def decorator_b(func):
    def wrapper(*args,**kwargs):
        print("B 前处理：进入内层")
        result = func(*args,**kwargs)
        print("B 后处理：离开内层")
        return result
    return wrapper

@decotator_a
@decorator_b

def say():
    print("-> 原始函数执行中")
    return "done"
print(say())
