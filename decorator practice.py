"""
假设你正在开发一个学生管理系统，里面有添加学生、查询学生等功能。
现在有个需求：
每次执行这些功能时，都要自动打印操作日志，显示：
- 执行了哪个函数。
- 执行前打印“开始执行”。
- 执行后打印“执行结束”。
如果每个函数都手动写这些打印语句，会有很多重复代码。因此，我们使用装饰器统一处理日志。
"""
# def log(func):
#     def wrapper(*args,**kwargs):
#         print(f"开始执行:{func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"执行结束：{func.__name__}")
#         return result
#     return wrapper
#
# @log
# def add_student(name):
#     print(f"添加学生：{name}")
#
# @log
# def find_student(name):
#     print(f"查询学生：{name}")
#
# add_student("张三")
# print("------------")
# find_student("李四")

#登录权限校验（Web 后端最常见的装饰器）
"""
假设有一个简单的个人中心：
- auth 保存当前用户的登录状态。
- is_login 为 False 时，访问个人中心返回 "403 未登录，请先登录！"。
- is_login 为 True 时，正常执行原函数，返回欢迎信息。
"""
#模拟当前用户登录状态
auth = {
    "is_login": False,
    "user": None
}

def login_required(auth_data):
    #第一层：接收登录状态字典
     def decorator(func):
         #第二层：接收原函数
         def wrapper(*args,**kwargs):
             #第三层：检查是否登录
             if not auth_data["is_login"] :
                 return f"403未登录，请先登录！"
             return func(*args,**kwargs)
         return wrapper
     return decorator

@login_required(auth)
def view_profile():
    return f"个人中心：欢迎{auth['user']}"

print(view_profile())

#修改登录状态
auth["is_login"] = True
auth["user"] = "yangxin"

#第二次调用
print(view_profile())

#多装饰器组合（日志 + 计时同时挂）

""" 
模拟一个下载程序。我们希望每次下载时自动打印日志，并统计下载耗时。
要求：
1. log：打印调用的函数名、位置参数和关键字参数。
2. timer：使用 time.perf_counter() 计算函数耗时。
3. 两个装饰器都要支持 *args、**kwargs。
4. 两个装饰器都要正确返回原函数的结果。
5. 使用 @log 和 @timer 组合装饰 download。
"""
import time

def log(func):
    def wrapper(*args,**kwargs):
        print(f"日志调用：{func.__name__},参数{args},{kwargs}")
        result = func(*args,**kwargs)
        return result
    return wrapper

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        print(f"计时：{func.__name__},耗时{time.perf_counter() - start:.4f}秒")
        return result
    return wrapper

@log
@timer
def download(size):
    time.sleep(3)
    return f"下载完成，共{size}MB"

print(download(100))

