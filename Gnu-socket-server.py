# 解释器位置
# -*- coding: UTF-8 -*-

import socket

#创建socket对象
socket_server = socket.socket()

#利用gethostname()函数获取主机地址
host = "localhost"
#设定一个端口号
port = 12345

#绑定IP和端口号
socket_server.connect((host,port))

#listen方法接收一个整数传参数，表示接受的连接数量，可不填
socket_server.listen()

#等待客户端连接，accept方法返回二元元组(连接对象, 客户端地址信息)
# accept()方法是阻塞式的方法，如果没有客户端连接，会一直等待，不往下执行
print("服务器已开始监听，正在等待客户端连接...")
connect_name,address = socket_server.accept()

print("接收到了客户端的连接，客户端的信息：{address}")

#接收客户端信息，使用客户端和服务端的本次连接对象，而非socket_server
while True:
    #接收消息
    data: str = connect_name.recv(1024).decode("UTF-8")
    print("客户端发来的的消息：{data}")

    #回复消息
    msg = input("请输入你要回复客户端的信息")
    if msg == 'exit':
        break
    connect_name.send(msg.encode("UTF-8"))

#关闭连接
connect_name.close()
socket_server.close()