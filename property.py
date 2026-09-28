# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#
#     def eat(self):
#         print("eating")
#     #只读
#     @property
#     def age(self):
#         # if self.__age > 18:
#         #     return 18
#         return self.__age
#     #读写
#     @age.setter
#     def age(self,age):
#         self.__age = age
#
#
# p1 = Person("张三",103)
# print(p1.name)
# # 改名之后访问
# #print(p1._Person__age)
# print(p1.age)
# p1.age = 23
# print(p1.age)


class Drink:
    """一杯奶茶：成本是商业机密，外面不能看"""
    def __init__(self,name,price,cost,sugar = "正常糖"):
        self.name = name
        self.sugar = sugar
        self.__price = price
        self.__cost = cost

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value <= 0:
            raise ValueError("价格必须大于0")
        self.__price = value

    def profit(self):
        #成本藏在内部，外面只能看到利润，不知道成本
        return self.__price - self.__cost


class Order:
    """一笔订单：结账逻辑藏在内部"""
    def __init__(self,table_no):
        self.table_no = table_no
        self.items = []

    def add(self,drink):
        self.items.append(drink)

    #私有方法：算小计
    def __subtotal(self):
        return sum(d.price for d in self.items)

    def __discount_money(self):
        total = self.__subtotal()
        return 5 if total >= 30 else 0

    @property
    #应付总价
    def total(self):
        return self.__subtotal() - self.__discount_money()

    def bill(self):
        print(f"---{self.table_no}号桌账单---")
        for d in self.items:
            print(f"{d.name}({d.sugar}) {d.price}元")
        print(f" 小计：{self.__subtotal()}元")
        print(f" 优惠：-{self.__discount_money()}元")
        print(f" 应付：{self.total}元")

order = Order("3")
order.add(Drink("珍珠奶茶", 12, 4))
order.add(Drink("拿铁", 15, 6))
order.add(Drink("芋泥波波", 16, 7))
order.bill()

print("访问控制")
tea = Drink("珍珠奶茶",12,4)
print(f"奶茶价格：{tea.price}")
tea.price = 122
print(f"涨价后售价：{tea.price}")
print(f"{tea.name}利润：{tea.profit()}")

































