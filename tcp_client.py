import socket
from socket import AF_INET, SOCK_STREAM

try:
    # Create a TCP/IP socket(AF = Address Family)
    client_socket = socket.socket(AF_INET, SOCK_STREAM)
    try:
        # 1.) Connect to the server (localhost = 127.0.0.1) 
        server_address = ('localhost', 8000)
        client_socket.connect(server_address)
        try:
            # 2.) Send message over to the TCP-Server
            message = 'Liano'
            client_socket.sendall(message.encode())

            # 3.) Receive Response from TCP-Server
            response = client_socket.recv(1024)
            print('Received:', response.decode())
      
      except Exception as e:
            print("Error occurred while transmitting data: ", e)
   
  except ConnectionRefusedError:
            print("Connention refused. Make sure the server is running")

    except Exception as e:
            print("An error occurred during connection")
   
  finally:
            # Closing the client socket
            client_socket.close()

        except Exception as e:
      print("An error occured: ", e)
