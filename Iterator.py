#迭代器
"""
“可迭代对象”是能交给 for 循环逐个取元素的对象，例如列表、元组、字符串、字典、集合、文件对象和生成器。
“迭代器”则像一个带当前位置的取号器：
- iter(对象)：拿到取号器。
- next(迭代器)：取下一个元素。
- 元素耗尽时，抛出 StopIteration。
- 迭代器通常只能向前走，不能自动倒退或重置。
- for 循环实际上替我们完成了 iter()、不断 next() 和处理 StopIteration

"""
from collections.abc import Iterable,Iterator

names = ["小明","小红","小丽"]

print("列表是否可迭代：",isinstance(names,Iterable))
print("列表本身是否是迭代器：",isinstance(names,Iterator))

it = iter(names)
print("\n手动取值：")
print(next(it))
print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration as e:
    print("没有更多元素了",e)

print("\n for循环的效果：")
for name in names:
    print(name)

#自定义迭代器
#倒序遍历传入的序列
class ReverseIterator:
    def __init__(self,data):
        self.data = data
        self.index = len(data) #用来标记当前要取的位置，初始等于元素个数，不是下标

    #for循环启动时，会自动调用
    #返回迭代器对象
    def __iter__(self):
        return self # 这里返回自己，代表当前这个实例本身就是迭代器

    #for循环每次拿取元素，都会自动调用next()
    def __next__(self):
        if self.index == 0:
            raise StopIteration # 条件：指针等于0，抛出迭代异常，遍历结束

        self.index -= 1 # 指针先减1
        return self.data[self.index] # 再返回对应下标的元素

#测试
tasks = ["写需求","开发功能","测试","上线"]
for task in ReverseIterator(tasks):
    print("执行：",task)

#ReverseIterator类的对象是迭代器
rev = ReverseIterator(tasks)
print(isinstance(rev,Iterator))#是迭代器

# 自定义倒计时迭代器
class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration # 数完了，通知for循环结束
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n,end = " ")


