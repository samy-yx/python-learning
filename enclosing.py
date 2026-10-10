#闭包
"""
闭包是“函数带着它创建时的外部数据一起离开”。外部函数执行结束后，内部函数仍记得它曾使用过的外部变量。
构成闭包的三个条件：
1. 有外部函数；
2. 外部函数中定义内部函数；
3. 内部函数引用外部变量，并作为结果返回。
"""

#练习：定制折扣计算器
def make_discount_calculator(rate):
    """返回一个记住rate的折扣计算函数。"""
    def calculate(price):
        return price * rate

    return calculate

vip_discount = make_discount_calculator(0.8)
student_discount = make_discount_calculator(0.9)

price = 100
print("原价：",price)
print("VIP价：",vip_discount(price))
print("学生价：",student_discount(price))

#带状态的闭包练习
def make_bank_account(initial_balance = 0):
    balance = initial_balance

    def operate(amount):
        nonlocal balance

        if balance + amount < 0:
            return f"余额不足，当前余额：{balance}"

        balance += amount
        return f"操作成功，当前余额：{balance}"
    return operate

account = make_bank_account(100)

print(account(50)) # 150
print(account(-30)) # 120
print(account(-200)) # 余额不足，120
