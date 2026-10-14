import multiprocessing
import time
#向文件写数据
def write_file():
    with open("test.txt","w") as f:
        while True:
        # for i in range(3):# 只写入3行
            f.write("Hello world\n")
            f.flush()
            time.sleep(0.5)

#从文件中读取数据
def read_file():
    with open("test.txt","r") as f:
        while True:
            time.sleep(0.5)
            print(f.readline())
            # char = f.read(1)
            # #如果读到空串，文件已经读完
            # if char == "":
            #     break
            # print(char,end = "",flush = True)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target = write_file)
    p2 = multiprocessing.Process(target = read_file)

    p1.start()
    p2.start()