import os

with open("a.txt","w",encoding = "utf-8") as file:
    file.write("计算机242-30-杨鑫")

# def func(filename):
#     try:
#         file = open("a.txt","r")
#     except Exception as err:
#         print(err)
#     else:
#         print(f"a.txt:{file.read()}")
#         file.close()
# func("file")

# with open("a.txt","r",encoding = "utf-8") as f1:
#     content = f1.read()
#     print(f"a.txt:{content}")
#
#
# with open("b.txt","w",encoding = "utf-8") as f2:
#     f2.write(content)
#
# with open("b.txt","r",encoding = "utf-8") as f2_read:
#     print(f"b.txt:{f2_read.read()}")


with open("a.txt","r",encoding = "utf-8") as f:
    text = f.read()

res = []
for ch in text:
    if ch.isdigit():
        res.append(ch)
print(res)

















