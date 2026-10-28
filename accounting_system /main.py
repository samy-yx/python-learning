from decimal import Decimal,InvalidOperation
from datetime import date #打印当前系统日期
from datetime import datetime
import uuid #模拟生成唯一标识符
import json

""""""
#判断金额是否合法
def check_amount(amount):
    try:
        #把传入的 amount（字符串，比如"14"、"99.99"）转成 Decimal 高精度小数
        d = Decimal(amount)
        # 判断：金额 <= 0 就不合法，返回False，不能是0、负数
        if d <= Decimal("0"):
            return False
        # d.as_tuple().exponent 拿到小数的指数
        # exponent < -2 代表小数位数超过2位，例如 1.234 有3位小数，exponent=-3
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
            print(f"金额：{bill['amount']}|{bill['bill_type']}|{bill['category']}|{bill['bill_date']}|{bill['remark']}")

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

#删除账单

def del_bills():
    bills = load_bills()


    if not bills:
        print("账单暂无记录")
    else:
        for index, bill in enumerate(bills):
            print(f"{index}. {bill['amount']} | {bill['bill_type']} | {bill['category']} | {bill['bill_date']} | {bill['remark']}")

        should_exit = False # 判断输入n后是否退出
        while True:
            try:
                del_index = int(input("输入要删除的账单号："))
            except ValueError:
                print("输入错误，请输入整数")
                continue
            if 0 <= del_index < len(bills):
                #删除确认


                while True:
                    confirm = input("确认删除吗？(y/n):").strip().lower()
                    if confirm == "y":
                        # 删除加保存账单
                        del bills[del_index]
                        save_bills(bills)
                        print(f"已删除{del_index}号账单")

                        # 如果删除完账单为空
                        if not bills:
                            print("账单已经全部删除，暂无记录")
                        else:
                            for index, bill in enumerate(bills):
                                print(
                                    f"{index}. {bill['amount']} | {bill['bill_type']} | {bill['category']} | {bill['bill_date']} | {bill['remark']}")
                        break
                    elif confirm == "n":
                        print("取消删除，退出删除帐单")
                        should_exit = True #准备退出外层循环
                        break

                    else:
                        print("输入错误,请输入y 或 n")
                if should_exit:
                    break

            else:
                print("输入不合法，重新输入")


def query_bills():
    bills = load_bills()
    if not bills:
        print("账单暂无记录")
    else:
        while True:
            query_type = input("请选择查看所有收入账单还是支出账单(收入/支出)：").strip()
            if not check_bill_type(query_type):
                print("输入错误，请重新输入！")
            else:
                found = False
                for index, bill in enumerate(bills):
                    if bill["bill_type"] == query_type:
                        found = True
                        print(f"{index}. {bill['amount']} | {bill['bill_type']} | {bill['category']} | {bill['bill_date']} | {bill['remark']}")

                if not found:
                    print("没有符合条件的账单")
                break

#修改账单
def modify_bills():
    bills = load_bills()
    if not bills:
        print("账单暂无记录")
    else:
        for index,bill in enumerate(bills):
            print(f"{index}. {bill['amount']} | {bill['bill_type']} | {bill['category']} | {bill['bill_date']} | {bill['remark']}")

        while True:
            try:
                modify_index = int(input("请输入要修改账单的序号："))
            except ValueError:
                print("输入错误，请重新输入整数")
                continue

            if 0 <= modify_index < len(bills):
                #修改菜单
                while True:
                    print("1.金额")
                    print("2.收支类型")
                    print("3.分类")
                    print("4.日期")
                    print("5.备注")
                    print("0.取消修改")

                    modify_type = input("请输入要修改的内容：")
                    if modify_type == "1":
                        while True:
                            amount = input("请输入金额：")
                            if check_amount(amount):
                                bills[modify_index]["amount"] = amount
                                save_bills(bills)
                                print("金额修改成功")
                                break
                            else:
                                print("金额不合法，请重新输入")

                    elif modify_type == "2":
                        while True:
                            bill_type = input("请输入收支类型：")
                            checked_type = check_bill_type(bill_type)
                            if checked_type:
                                bills[modify_index]["bill_type"] = checked_type
                                save_bills(bills)
                                print("收支类型修改成功")
                                break
                            else:
                                print("收支不合法，请重新输入")

                    elif modify_type == "3":
                        category = input("请输入分类：").strip()

                        bills[modify_index]["category"] = category
                        save_bills(bills)
                        print("分类修改成功")


                    elif modify_type == "4":
                        bill_date = input("请输入日期：")

                        bills[modify_index]["bill_date"] = bill_date
                        save_bills(bills)
                        print("日期修改成功")


                    elif modify_type == "5":
                        remark = input("请入备注：")

                        bills[modify_index]["remark"] = remark
                        save_bills(bills)
                        print("备注修改成功")


                    elif modify_type == "0":
                        print("退出修改账单")
                        break
                    else:
                        print("输入错误，重新输入")
                break
            else:
                print("输入不合法，请重新输入")


if __name__ == "__main__":
    while True:
        print("1. 新增账单")
        print("2. 查看账单")
        print("3. 统计收支")
        print("4. 删除账单")
        print("5. 查询账单")
        print("6. 修改账单")
        print("0. 退出程序")

        choice = input("请选择操作:")
        if choice =="1":
            add_bill()
        elif choice == "2":
            show_bills()
        elif choice == "3":
            statistics_bills()
        elif choice == "4":
            del_bills()
        elif choice == "5":
            query_bills()
        elif choice == "6":
            modify_bills()
        elif choice == "0":
            print("退出程序")
            break
        else:
            print("输入错误，请重新输入")





