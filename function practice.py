#不定长"位置"参数
"""
def 函数名(普通参数, *args):
    函数体

1. 调用时，**多出的位置参数全部放进 args 元组**
2. 普通参数必须写在`*args`前面
3. 如果`*args`后面还有形参，后面参数**必须用关键字传参**
4. 没有多余参数传入，`args`是空元组 `()`
"""
def printInfo(num,*vartuple):
    print(num)
    print(vartuple) #以元组形式输出

printInfo(70,60,50)


def sum_num(base,*args):
    total = base
    for num in args:
        total += num
    return total
print(sum_num(10,1,2,3))

def print_names(leader,*members):
    print(f"组长{leader}")
    print(f"组员{members}")

print_names("张三", "李四", "王五", "赵六")

#不定长关键字参数
"""
def 函数名(普通参数, **kwargs):
    函数体

1. 接收所有 `key=value` !关键字!参数，打包成**字典**
2. `**kwargs` **必须放在所有参数的最后**，后面不能再加参数
3. 不传关键字参数，`kwargs`是空字典 `{}`
"""

def create_user(name,age,**kwargs):
    user = {"name":name,"age":age}
    user.update(kwargs)
    print(user)
create_user("小明",19)
create_user("小红", 20, city="大连", hobby="篮球", height=165)

