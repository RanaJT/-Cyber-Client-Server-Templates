import socket
from socket import AF_INET, SOCK_STREAM

# Create a TCP/IP socket(AF = Address Family)
client_socket = socket.socket(AF_INET, SOCK_STREAM)

# 1.) Connect to the server (localhost = 127.0.0.1) 
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# 2.) Send message over to the TCP-Server
message = 'Liano'
client_socket.sendall(message.encode())

# 3.) Receive Response from TCP-Server
response = client_socket.recv(1024)
print('Received:', response.decode())

# Closing the client socket
client_socket.close()