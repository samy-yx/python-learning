import multiprocessing


def greet(name,age):
    print(f"你好，我叫{name},今年{age}岁")

if __name__ =="__main__":
    p = multiprocessing.Process(
        target = greet,
        args = ("小明",20),
        name = "问候进程"
    )

    p.start()
    print(p.name)#查看进程名字
    print(p.pid) #获取进程ID
    print(p.is_alive()) #如果进程正在运行，通常返回 True；如果已经结束，返回 False
    p.join() #等待指定的子进程结束

    print("子进程执行完毕")