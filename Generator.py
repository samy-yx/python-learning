#generator:生成器
"""
生成器是"按需生产数据"的迭代器，普通函数用return后会结束，
生成器函数遇到 yield 后会暂停，并且交出一个值，并记住现场，下次取值时会从暂停处继续

类比：普通函数像是一次性把整箱矿泉水搬到桌上；生成器像饮水机，每次需要一杯才接一杯
生成器适合无限序列，大文件，分页数据和大量任务

核心概念：
- 生成器是"用于创建迭代器的简单而强大的工具"，写法像函数，但用yield返回数据
- 每次调用next()或for迭代，函数从上次暂停的地方继续，知道再次遇到yield
- 创建方式：
    -①:生成器表达式 (x for x in range(5)) ; ②：含yield的函数
- 函数里 return 的值会作为StopIteration 异常的附带信息，用try/except StopIteration as e 捕获
- yield不止可以"产出"，也可以"接收"，注意，刚创建的生成器尚未运行到yield,所以第一次必须使用
    next(g)[启动 / 推进生成器，执行到下一个 yield，拿到 yield 产出的值]或者g.send(None)启动，不能直接g.send("内容")
- send(value)：恢复并执行生成器"发送"一个值，这个值会成为当前yield表达式的值 -- 实现生成器和外部双向通信
- 用send()启动生成器时必须传send(None)，因为第一个yield之前没有可接受值的表达式

"""
"""
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n # 暂停在这里，把n交出去
        n += 1
for num in count_up_to(5):
    print(num,end = " ")

print()
#捕获生成器return 的值
def fibo(n):
    a,b,counter = 0,1,0
    while counter < n:
        yield b
        a,b,counter = b,a + b, counter + 1

    return "done" # 结束信号，藏在StopIteration里

f = fibo(5)

try:
    while True:
        print(next(f),end = " ")
except StopIteration as result:
    print("\n结束：",result) # done

# 双向通信 -- 给生成器"递纸条"
def recv_and_echo():# receive and echo 接受和回显
    name = yield "请输入你的名字"
    yield f"你好，{name}！"

g = recv_and_echo()
print(next(g))
print(g.send("张三"))
"""
####################################################################################################
# 生成前 N 个斐波那契数
def fibonacci(count):
    a,b = 0,1
    for _ in range(count):
        yield b
        a,b = b,a + b
    return "生成完毕"
generator = fibonacci(23)
try:
    while True:
        print(next(generator),end = " ")
except StopIteration as error:
    print(error.value)


#生成器表达式练习

#列表表达式会立刻计算并保存所有结果
squares_list = [x * x for x in range(10)]

#生成器表达式会按需计算
squares_generator = (x * x for x in range(10))

print("列表：",squares_list)
print("生成器地址：",squares_generator)
print("生成器逐个取值：")
for value in squares_generator:
    print(value,end = " ")
print()
# send():向生成器传值

#模拟一个可切换模式的计数器
def counter():
    number = 0
    step = 1

    while True:
        command = yield number

        if command == "fast":
            step = 10
        elif command == "normal":
            step = 1
        elif command == "reset":
            number = 0
            continue
        number += step

g = counter() # 创建生成器对象，内部函数不会执行
print(next(g)) # 启动生成器，执行代码停到yield断点，接收参数
print(g.send("normal")) # 1
print(g.send("fast")) # 11
print(g.send("fast")) # 21
print(g.send("reset")) # 0