# -*- coding: utf-8 -*-
import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
socket_server.bind((ip_address, 22))
socket_server.listen(2)

con, address = socket_server.accept()
print(f"接收到了客户端的链接,客户端的信息是:{address}")

while True:
    data = con.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是:{data}")

    if data == 'exit':
        break

    msg = input("请输入你要和客户端回复的消息: ").encode("UTF-8")
    con.send(msg)

con.close()
socket_server.close()
