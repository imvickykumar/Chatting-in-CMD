import socket

def client_program():
    # host = socket.gethostname()
    # host = '192.168.43.100'
    
    host = '192.168.43.213'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("\n                             -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(' -> ' + data)
        message = input("                             -> ")

    client_socket.close()
    
if __name__ == '__main__':
    client_program()