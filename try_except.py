"""
规则：没异常，跳过except继续走；有异常，跳过try剩下的代码，执行except。
except不写类型是通配的意思，什么异常都接
"""
"""
try:
    result = 3 / 0
    print("没有发生异常")
except:
    print("发生异常")
print("END")

#捕获指定类型 + 获取异常描述
try:
    result = 3 / 0
except ZeroDivisionError as e: # as e 拿到异常描述
    print(e) # 打印异常描述
    print("除数不能为0")
except (RuntimeError,TypeError,NameError) as e:
    print(e)
except:
    print("Unexpected Error") # 没有预期的错误


# else : 没异常时才执行的代码
try:
    result = 3/0
except ZeroDivisionError :
    print("除数不能为0")
else:
    print(f"正确结果是{result}")

# finally:无论是否异常都执行
try:
    result = 3 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally")
print("END")


# !!! raise:主动抛出异常
def int_add(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x + y
    else:
        raise TypeError("参数类型错误") # 主动制造异常，交给调用方处理
print(int_add(1,2))
print(int_add("1","2"))
"""

# with:
# with open("test.txt","w") as f:
#     f.write("helo python")
# print(f.closed)

try:
    with open("test.txt","r",encoding = "utf-8") as f:
        data = f.read()
except FileNotFoundError as e:
    print("文件不存在：",e)
else:
    print(data)
finally:
    print("资源已自动释放")
