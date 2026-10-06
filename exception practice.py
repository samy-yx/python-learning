#写一个除法函数，除数为 0 时不崩溃，而是打印异常描述
# def divide(a,b):
#     try:
#         return  a / b
#     except ZeroDivisionError as e:
#         print("出错，除数不能为0")
# print(divide(2,3))
# print(divide(3,0))

"""练习 2（综合）：让用户输入整数，用上 try/except/else/finally 四种结构，
处理 "输入非数字" 和 "除数为 0" 两种情况。
"""
while True:
    try:
        num = int(input("请输入一个整数："))
        result = 100 / num
    except ValueError:
        print("输入的不是整数！")
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print(f"100 ÷ {num} = {result}")
        break
    # finally:
    #     print("程序结束")

#自定义异常 + with，模拟 "设置年龄必须合法

class AgeError(Exception): # 继承父类Exception
    pass

def set_age(age):
    if not isinstance(age,int) or not (0 <= age <= 100):
        raise AgeError(f"年龄不合法：{age}")
    return age

try:
    set_age(200)
except AgeError as e:
    print(type(e))
    print("捕获到自定义异常：",e)


with open("test.txt","w",encoding = "utf-8") as f:
    f.write("Hello Python ~~~~~~~~~~~~~~~~~~~~~~")
print("文件已经写入并自动关闭")
