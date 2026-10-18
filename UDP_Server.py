#UDP通信服务器开发

import socket

# 创建socket对象
udp_socket = socket.socket(socket.AF_INET,type = socket.SOCK_DGRAM)
#绑定ip和端口号
udp_socket.bind(('0.0.0.0',8888))
#循环
while True:
    #接收客户端发送的消息
    recv_data,client_info = udp_socket.recvfrom(1024)
    client_ip = client_info[0] # ip
    client_port = client_info[1] #端口号
    print(f"客户端{client_ip}:{client_port}说:{recv_data.decode("utf-8")}")
    #向客户端发送数据
    udp_socket.sendto("你好，消息已经收到".encode("utf-8"),client_info)

#关闭套接字
udp_socket.close()