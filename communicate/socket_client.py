import socket

# 创建一个 TCP Socket 客户端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器的 IP 地址和端口号
server_ip = "10.0.8.55"  # 替换为实际的服务器 IP 地址
server_port = 22  # 替换为实际的服务器端口号

# 连接到服务器
client_socket.connect((server_ip, server_port))
while True:
    # 发送数据到服务器
    message = input("请输入你要发送的消息: ")
    if message == "exit":
        break
    else:
        client_socket.sendall(message.encode())

    # 从服务器接收数据
    received_data = client_socket.recv(1024).decode()
    print("接收到了客户端的链接,服务器返回的数据是:", received_data)
# 关闭 Socket 连接
client_socket.close()
