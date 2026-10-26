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
    if bill_type == "收入" or bill_type == "支出":
        if bill_type == "收入":
            bill_type_en = "income"
        else:
            bill_type_en = "expense"
        return bill_type_en
    else:
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
    bill_type = input("请输入收支类型：").strip() # strip()：去除字符串首尾空白
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
            #datetime.strptime:验证日期，在日期无法解析时抛出ValueError
            date_text = datetime.strptime(date_input, "%Y-%m-%d")
            bill_date = date_input
            break
        except ValueError:
            print("日期无效,请重新输入")
print(bill_date)


#备注
remark = input("请输入备注:").strip()

print(f"备注是：{remark}")

bill = {}
bill["id"] = uuid.uuid4().hex
bill["amount"] = amount
bill["bill_type"] = result
bill["category"] = category
bill["bill_date"] = bill_date
bill["remark"] = remark
print(bill)



#完整保存账单
bills = load_bills()
bills.append(bill)
save_bills(bills)





