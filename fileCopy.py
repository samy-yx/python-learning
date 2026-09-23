# def file_copy(src,dest):
#     #打开源文件
#     src_file = open(src,"rb")
#     #以二进制读取文件
#     content = src_file.read()
#     #打开目标文件
#     dest_file = open(dest,"wb")
#     #以二进制写文件
#     dest_file.write(content)
#     #关闭源文件
#     src_file.close()
#     #关闭目标文件
#     dest_file.close()
#
# file_copy("d:\\小白.png","e:\\小白.png") #注意：一个\是转义字符，得两个\\

#优化


def file_copy(src,dest):
    # 打开源文件和目标文件
    src_file = open(src,"rb")
    dest_file = open(dest,"wb")

    #边读边写，每次读取1024字节(1KB)，防止一次性读大文件占满内存
    while content := src_file.read(1024):
        dest_file.write(content)

    #关闭源文件和目标文件
    src_file.close()
    dest_file.close()
file_copy("d:\\小白.png","e:\\小白.png")


