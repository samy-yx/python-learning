#解包传参
#简单理解：一个整体的数据，拆开交给函数
"""
*：解包位置参数,list、tuple
**：解包关键字参数,dict
"""
#学生信息打印器
# student = {
#     "name": "小明",
#     "age": 20,
#     "major": "计算机科学与技术"
# }
# def student_info(name,age,major):
#     print("姓名：", name)
#     print("年龄：", age)
#     print("专业：", major)
#
# #student_info(**student)
#
# scores = [85, 90, 78, 92, 88]
#
#
# def print_scores(a, b, c, d, e):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#
# print_scores(*scores)

###
#防止函数修改列表，使用deepcopy(深拷贝)

import copy
numbers = [10, 20, [30, 40]]

def add_number(data):
    data[2].append(50)
    print("函数内部",data)

print("函数外部",numbers)
add_number(copy.deepcopy(numbers))
print("处理后",numbers)