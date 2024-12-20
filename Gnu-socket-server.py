# 解释器位置
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connet((host,port))
print (s.recv(1024))
s.close()