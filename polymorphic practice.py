## 多态：同一个方法，不同对象调用，表现出不同的行为

# 1. 定义两个没有继承关系的类
class Dog:
    def speak(self):
        print("汪汪")
class Cat:
    def speak(self):
        print("喵喵")

#同一个函数：接受任意拥有speak()方法的对象
def make_speak(animal):
    animal.speak()
dog = Dog()
cat = Cat()

#不管传入的是dog还是cat，只要有speak就能跑
make_speak(dog)
make_speak(cat)

# 2.基于继承的经典多态
"""
父类定义接口（speak）
子类重写 (override)该方法
同一个函数调用，不同子类，执行不同代码
"""
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵")

def make_speak(animal:Animal):#类型注解：推荐传入Animal类的实例对象，或者是它子类实例
    animal.speak()

dog = Dog()
make_speak(dog)
