#一个类里同名方法重写，后面的覆盖前面的
# class student:
#     def eat(self,a):
#         print("eating")
#     def eat(self,a,b):
#         print("eating 1234")
#
# s = student()
# s.eat(1,2)
## 核心用途：子类覆盖父类方法
class animal:
    def speak(self):
        print("动物叫")
class Dog(animal):
    def speak(self):
        print("汪汪汪")

class Cat(animal):
    def speak(self):
        print("喵喵喵")

for animal in [Dog(),Cat()]:
    animal.speak()
####################################################################
#super 在多继承中的使用
class Parent1:
    def __init__(self,value1,**kwargs):
        print("Initializing Parent1")
        super().__init__(**kwargs)
        self.value1 = value1

class Parent2:
    def __init__(self,value2,**kwargs):
        print("Initializing Parent2")
        super().__init__(**kwargs)
        self.value2 = value2

class Child(Parent1,Parent2):
    def __init__(self,value1,value2):
        print("Initializing Child")
        super().__init__(value1 = value1,value2 = value2)
print(Child.__mro__)

child = Child( "value from Parent1", "value from Parent2")
print(child.value1)
print(child.value2)