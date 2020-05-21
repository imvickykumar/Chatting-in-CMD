import socket

def server_program():
    # host = socket.gethostname()
    # host = '192.168.43.213'
    
    host = '192.168.43.100'
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    # print("Connection from: " + str(address), end = '\n\n')
    print()
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
            
        print(" -> " + str(data))
        data = input('                             -> ')
        conn.send(data.encode())
        
    conn.close()

if __name__ == '__main__':
    server_program()