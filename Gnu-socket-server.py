# 解释器位置
# -*- coding: UTF-8 -*-

import socket
import time

#创建socket对象
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#设定一个端口号
port = 8888

#绑定IP和端口号
socket_server.bind(('192.168.26.1',port))
print("UDP服务已经启动，等待发送消息")

# 预定义消息列表
messages = ["hello",  "\n","zhouxiang!", "How are you?", "55555", "Test message"]

print("UDP 服务已启动，开始自动发送消息...")

try:
    while True:
        for msg in messages:
            # 发送消息
            socket_server.sendto(msg.encode("UTF-8"), ('192.168.26.134', 8081))
            print(f"已发送消息：{msg}")
            time.sleep(0.1)  # 每次发送间隔时间
except KeyboardInterrupt:
    print("程序已手动终止。")


# while True:
#     # data = socket_server.recvfrom(1024)[0].decode("UTF-8")
#     # print(f"客户端发来的消息为 {data}")
#     send_msg = input("请输入要发送给该客户端的消息：")
#     socket_server.sendto(send_msg.encode("UTF-8"),('192.168.26.134',8081))
