###实验一 pytthon基础

"""
# 1.列表，lambda函数，map函数
nums1 = [1,2,3]
nums2 = [4,5,6]
nums3 = [7,8,9]
print("Original list:")
print(nums1)
print(nums2)
print(nums3)

result = map(lambda x,y,z:x + y + z,nums1,nums2,nums3)
print("\nNew list after adding above threer lists:")
print(list(result))


#循环，选择结构
true_number = int(input("请输入数字:"))
low_number = int(input("请输入范围下限："))
high_number = int(input("请输入范围上限："))

i = 1
while i <= 5:
    guess_number = int(input(f"数字的范围是:{low_number}-{high_number},现在是第{i}次猜测"))
    if true_number == guess_number:
        print("猜对")
        break
    elif guess_number < true_number and guess_number > low_number:
        low_number = guess_number
    elif guess_number > true_number and guess_number < high_number:
        high_number = guess_number
    i = i + 1
if i > 5:
    print(f"很遗憾，你五次都没有猜对。正确数字是{true_number}。")

import random

number = random.randint(1,101)
print(number)

count = 0
n = 7
while True:
    guess = int(input(f"请输入一个1~100的数字,还剩{n}次机会:"))
    count += 1
    n -= 1
    if guess == number:
        print("猜对")
        print(f"你一共猜了{count}次")
        break
    elif guess > number:
        print("猜大了")
    else:
        print("猜小了")


#用户登录验证
#创建列表存放用户名和密码
users = ["zhangsan","lisi","wangwu","zhaoliu"]
password = ["123","456","abc","qwe"]
while True:
    inuser = input("请输入用户名：")
    inpsw = input("请输入密码：")
    if inuser in users:
        index = users.index(inuser)
        if password[index] == inpsw:
            print("输入正确！")
            break
        else:
            print("密码错误，请重新输入！")
            continue
    else:
        print("不存在该用户，请重新输入！")


# 字典，循环结构
student_score = {}
while True:
    #输入姓名
    name = input("请输入学生姓名（按Q退出）：")
    if name == "Q" or name == "q":
        break
    #输入成绩
    score = float(input("请输入学生成绩:"))
    if score >= 90:
        rating = "优秀"
    elif score >= 80:
        rating = "良好"
    elif score >= 60:
        rating = "及格"
    else:
        rating = "不及格"
    #对字典的键进行赋值操作
    student_score[name] = rating
    print(f"学生成绩单为：{student_score}")

#5 函数，循环 - 账号注册检测

#检测用户名是否符合要求
def uncheck(username):
    if len(username) == 0:
        return False
    else:
        return True

#检查密码是否符合要求
def pwcheck(password):
    if len(password) >= 6:
        return True
    else:
        return False

#创建一个空字典保护用户名和字典
accounts = {}
#保存函数
def save(username,password):
    #用户名和密码都通过检测
    if uncheck(username) == True and pwcheck(password) == True:
        accounts[username] = password
        print("账号创建成功！")

for i in range(3):
    username = input("请输入用户名:")
    password = input("请输入密码：")
    save(username,password)

print(accounts)


#6.函数。循环.选择结构 - order点单（可变参数）

def order(table,*menu):
    print('********************************')
    print(f"{table}号桌订单",end = " ")
    for staff in menu:
        print(staff,end = " ")
    print('\n********************************')

order('04', '杏脯', '花茶', '普洱', '果盘')
order('13', '酒鬼花生', '桂花酒', '龙井茶', '果盘')
"""

# 随机函数 - 模拟投掷硬币
import random
#记录正面
a = 0
num = int(input("请输入投掷的次数："))
for i in range(num):
    rand = random.randint(0,1)
    if rand == 0:
        a += 1
#反面
b = num - a
print(f"正面{a}次，反面{b}次")














