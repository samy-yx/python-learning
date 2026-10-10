#命名空间与作用域
"""
Python 查找变量遵循 LEGB 顺序：
1. Local：当前函数的局部作用域。
2. Enclosing：外层函数作用域。
3. Global：当前模块的全局作用域。
4. Built-in：内置作用域，例如 len、print。

关键规则（文档原文要点）：

- 在最内层作用域访问外层 / 全局变量时，不声明 global/nonlocal 就是只读；尝试写入会创建一个新的局部变量，外部的同名变量不受影响。
- global 声明 "这个变量是全局的，要在全局作用域重新绑定"。
- nonlocal 声明 "这个变量在外层函数作用域，要改外层的"。
"""
name = "全局名字"
def outer():
    name = "外层名字"

    def inner():
        name = "局部名字"
        print("inner 内部：",name)

    inner()
    print("outer 内部",name)
outer()
print("模块全局：",name)
print("\n ----- global示例 -----")
n = 100
def try_change():
    n = 200 # 这里创建了局部 n，全局 n 没动
try_change()
print(n) # 100

# 生命global才能改全局
count = 0
def add_one():
    global count # 声明：改的是全局的 count
    count += 1
add_one()
add_one()
print(count) # 2



print("\n ----- nonlocal示例 -----")
def make_counter():
    count = 0

    def add_one():
        nonlocal count
        count += 1
        return count
    return add_one

counter = make_counter()
print(counter())
print(counter())
print(counter())
