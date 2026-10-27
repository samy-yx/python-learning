from decimal import Decimal,InvalidOperation
from datetime import date #打印当前系统日期
from datetime import datetime
import uuid #模拟生成唯一标识符
import json

""""""
#判断金额是否合法
def check_amount(amount):
    try:
        d = Decimal(amount)
        if d <= Decimal("0"):
            return False
        if d.as_tuple().exponent < -2:
            return False
        return True
    except InvalidOperation:
        return False



#判断收支类型是否合法
def check_bill_type(bill_type):
    # if bill_type == "收入" or bill_type == "支出":
    #     if bill_type == "收入":
    #         bill_type_en = "收入"
    #     else:
    #         bill_type_en = "支出"
    #     return bill_type_en
    # else:
    #     return False
    bill_type = bill_type.strip()
    valid_types = {"收入","支出"}
    if bill_type in valid_types:
        return bill_type
    return False

#检查账单是否为空
def load_bills():
    try:
        with open("bill.json", "r", encoding="utf-8") as f:
            original_bills = json.load(f)
            return original_bills
    except FileNotFoundError:
        #如果文件不存在/文件是空的，初始化空列表
        # bills = []
        # return bills
        return []


#保存账单
def save_bills(bills):
    with open("bill.json","w",encoding = "utf-8") as f:
        json.dump(bills,f,ensure_ascii = False,indent = 4)



#添加账单
def add_bill():
    #bill = {}不能卸载函数外面，都会修改同一个外部字典。如果你以后连续新增多笔账单，这个字典会被反复修改，可能导致之前追加进列表的账单也被改变
    bill = {} # 写在函数内部，每次新增一个账单都需要一个全新的字典

    # 输入金额
    while True:
        amount = input("请输入金额:")
        if check_amount(amount):
            print("输入成功")
            break
        else:
            print("金额不合法，请重新输入")

    # 输入收支类型
    while True:
        bill_type = input("请输入收支类型：").strip()  # strip()：去除字符串首尾空白
        result = check_bill_type(bill_type)
        if result:
            print("输入成功")
            print(result)
            break
        else:
            print("输入错误，请重新输入")

    # 输入分类
    while True:
        category = input("请输入分类：").strip()

        if not category:
            print("输入不能为空，请重新输入")
        else:
            print("输入成功")
            break

    # 日期
    bill_date = date.today().isoformat()
    while True:
        date_input = input("请输入账单日期(直接回车使用今天)：").strip()
        if not date_input:  # 如果为空：直接使用今天
            bill_date = date.today().isoformat()
            break
        else:
            try:
                # datetime.strptime:验证日期，在日期无法解析时抛出ValueError
                date_text = datetime.strptime(date_input, "%Y-%m-%d")
                bill_date = date_input
                break
            except ValueError:
                print("日期无效,请重新输入")


    # 备注
    remark = input("请输入备注:").strip()

    bill["id"] = uuid.uuid4().hex
    bill["amount"] = amount
    bill["bill_type"] = result
    bill["category"] = category
    bill["bill_date"] = bill_date
    bill["remark"] = remark


    # 完整保存账单
    bills = load_bills()
    bills.append(bill)
    save_bills(bills)


#展示账单
def show_bills():
    bills = load_bills()#调用load_bills():检查账单是否为空
    if not bills:
        print("暂无账单记录")
    else:
        for bill in bills:
            print(f"金额：{bill["amount"]}|{bill['bill_type']}|{bill['category']}|{bill['bill_date']}|{bill['remark']}")

#统计收支
def statistics_bills():
    bills = load_bills()
    total_income = 0
    total_expense = 0
    for bill in bills:
        amount = Decimal(bill["amount"])
        # 如果是收入，就累加到 total_income
        if bill["bill_type"] == "收入":
            total_income += amount
        # 如果是支出，就累加到 total_expense
        elif bill["bill_type"] == "支出":
            total_expense += amount
    # 结余
    balance = total_income - total_expense
    print(f"总收入：{total_income}。总支出：{total_expense}。结余：{balance}")


# bills = load_bills()
# 
# for index,bill in enumerate(bills): # enumberate:遍历列表，获取序号和元素
#     print(f"{index}. {bill['bill_type']} | {bill['category']} | {bill['amount']}元")
# 
# def delete_bill():
#     bills = load_bills()
# 
#     for index, bill in enumerate(bills):  # enumberate:遍历列表，获取序号和元素
#         print(f"{index}. {bill['bill_type']} | {bill['category']} | {bill['amount']}元")
# 
#         sequence_number = int(input("输入要删除的账单序号："))
#         index = sequence_number - 1
#         if 0 <= index <= len(bills) - 1 :
#             del bills[index]






if __name__ == "__main__":
    while True:
        print("1. 新增账单")
        print("2. 查看账单")
        print("3.统计收支")
        print("0. 退出程序")

        choice = input("请选择操作:")
        if choice =="1":
            add_bill()
        elif choice == "2":
            show_bills()
        elif choice == "3":
            statistics_bills()
        elif choice == "0":
            print("退出程序")
            break
        else:
            print("输入错误，请重新输入")





