# 浅拷贝与深拷贝
"""
浅拷贝：copy.copy(a):只复制最外层容器，内部嵌套的"可变"对象仍然公用
深拷贝：copy.deepcopy(a):递归复制内部可变对象，彼此独立
特殊情况：数字、字符串等原子类型对象 "无法拷贝"（拷贝前后 id 一样）；只含原子类型元素的元组也不能深拷贝（id 不变）
"""
import copy

original = {
    "name":"小王",
    "score":[90,88],
    "profile":{"city":"上海"}
}
alias = original
shallow = copy.copy(original)#浅拷贝
deep = copy.deepcopy(original)#深拷贝

#修改最外层不可变值：相当于让original["name"]指向新的字符串
original["name"] = "小李"

#修改内层嵌套的可变对象
original["score"].append(100)
original["profile"]["city"] = "杭州"

print(f"Original:",original)
print(f"Alias:",alias)
print("shallow:",shallow)
print("deep:",deep)

print("\n是否共享内部数据 score 列表")
print("original 与 shallow:",original["score"] is shallow["score"])
print("original 与 deep:",original["score"] is deep["score"])