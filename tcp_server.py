import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 1.) Binding. (binding the socket to a port and address)
server_address = ('127.0.0.1', 8000)
# ip = '127.0.0.1'
# port= 8000
server_socket.bind(server_address) # socket addressing

# Listening for any connection attempts for clients
server_socket.listen(1)

print('Server is listening on', server_address)

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    decoded_data = data.decode()
    print('Received:', decoded_data)

    # Send a response back to the client
    response = f'Your data has been recieved. Welcome, {decoded_data}.'
    client_socket.sendall(response.encode())

    # Close the client socket
    client_socket.close()