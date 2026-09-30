"""
# *arg:收集位置参数,打包成元组
def func(*args):
    print(args)
func(1,2,3) #(1,2,3)
func("a","b")#("a" ,"b")
func()#()

# **kwargs:收集关键字参数，打包成字典
def func(**kwargs):
    print(kwargs)
func(x = 1,y = 2)#{'x': 1, 'y': 2}
func(name = "张三",age = 18)#{'name': '张三', 'age': 18}
func()#{}


# 拆包
def add(a,b,c):
    return a + b + c

nums = (1,2,3) #元组
print(add(*nums)) # 把元组拆开 -> add(1,2,3)

def show(name,age):
    print(f"{name}:今年{age}岁")
info =[ {"name":"李四","age": 18},{"name":"张三","age":19}]
for item in info:
    show(**item)

## 普通参数 → *args→ **kwargs，位置不能乱。
def student(name,*scores,**info):
    print(f"姓名：{name}")
    print(f"成绩:{scores}")
    print(f"其他:{info}")
student("王五",90,53,43,班级 = "三班",学号 = "001")
"""

#通用日志函数
def log(msg,*args,**kwargs):
    print(f"[日志]{msg}",args,kwargs)
    log("用户登录","ip = 127.0.0.1",level = "INFO",time = "10:00")








































