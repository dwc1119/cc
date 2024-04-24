import socket

# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('111.227.237.82', 4022)
client_socket.connect(server_address)

# 发送数据
data = 'Hello, Server!'
client_socket.sendall(data.encode())

# 接收数据
response = client_socket.recv(1024)
print('接收到的数据:', response.decode())

# 关闭连接
client_socket.close()
