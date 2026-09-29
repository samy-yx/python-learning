"""
#1.9*9乘法表
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{j}*{i}={i*j}",end = "\t")
    print()


# 2.构造单词列表，获取列表中最长单词的长度
list = []
while True:
    word = input("请输入单词(按q退出)：")
    if word == "q":
        break
    list.append(word)
print(list)
#3.最大长度单词
# len_max = list[0]
# for i in list[1:]:
#     if len(i) > len(len_max):
#         len_max = i
len_max = max(len(word) for word in list)
for i in list:
    if len_max == len(i):
        long_word = i
        break


print(f"列表中最大单词长度是{len_max}，该单词是{long_word}")\



# 4.定义一个函数，函数参数为小于10000的正整数，分解各位数字，并以一个元组形式返回。在主程序中调用这个函数。
def split_num(num):
    res = []
    while num > 0:
        n = num % 10 #取出最后一位
        res.append(n)#放入数组
        num //= 10#去掉最后一位
    res.reverse()#反转，低位变高位
    return tuple(res)
print(split_num(12354))

#5.输入n，保留pi的n位小数
import math
n = int(input("请输入要保留的小数位数："))
print(round(math.pi,n))



#6.生成30个随机数据，模拟一个班的考试成绩(40-100分)。计算这批数据的平均分，最高分和
#最低分，并排序由高到低输出
import random
score =[]
for i in range(31):
    score.append(random.randint(40,100))
print(score)
avg = sum(score)/len(score)
max_score = max(score)
min_score = min(score)
score_sort = sorted(score,reverse = True)
print(f"成绩排序：{score_sort}")
print(f"平均分：{avg:.2f},最高分：{max_score},最低分：{min_score}")
"""

#7.实现一个人机石头剪刀布的游戏，读用户键盘输入，输出游戏结果

import random
slect = ["石头","剪刀","布"]
while True:
    user = input("请输入石头/剪刀/布(按q退出):")
    if user == "q":
        break
    computer = random.choice(slect)
    print(f"电脑出：{computer}")
    if user == computer:
        print("平局")
    elif (user == "石头" and computer == "剪刀") or (user == "剪刀" and computer == "布") or (
            user == "布" and computer == "石头"):
        print("你赢")
    else:
        print("你输")









