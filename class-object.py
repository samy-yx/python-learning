# class Person:
#     home = "earth"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("eatting")
#     def drink(self):
#         print("drinking")
#
# zs = Person("zs",19)
# print(zs.home)
# zs.eat()
# zs.drink()

"""
定义一个名为 Dog 的类，该类有两个属性 name（名字）和 age（年龄），以及一个方法 bark（叫），
bark 方法打印出 “Woof! My name is [name] and I am [age] years old.”。
创建一个 Dog 类的对象，并调用 bark 方法
"""
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"Woof! My name is {self.name} and I am {self.age} years old.")
#
# wangcai = Dog("wangcai",3)
# wangcai.bark()

##学生类
class Student:
    """学生类"""
    school = "金川小学"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"大家好，我是{self.name}，今年{self.age}岁，来自{Student.school}")
    @classmethod
    def show_school(cls):
        print(f"我们学校是{cls.school}")
    @staticmethod
    def is_doult(age):
        return age >= 18

student1 = Student("小明",9)
student1.introduce()
student1.show_school()
print(student1.is_doult(20))