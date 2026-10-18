#UDP通信客户端开发

import socket

#创建套接字对象
udp_socket = socket.socket(socket.AF_INET,type = socket.SOCK_DGRAM)

server_ip = "127.0.0.1"
server_port = 8888

#循环
while True:
    #向服务器发送数据
    udp_socket.sendto(input("对服务器说：").encode("utf-8"),(server_ip,server_port))
    #接收服务器数据
    recv_data,server_info = udp_socket.recvfrom(1024)
    print(f"服务器{server_port}说：{recv_data.decode("utf-8")}")

#关闭套接字
udp_socket.close()
