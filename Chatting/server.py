import socket

def server_program():

    host_name = socket.gethostname()
    host = socket.gethostbyname(host_name)
    
    print('\nHost IP is : ', host)
    port = 5000
    print('\nWaiting for receiver...\n')
    
    server_socket = socket.socket()
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    
    print("Connection from: " + str(address), end = '\n\n')
    message = 'hi'
    
    while message.lower().strip() != 'bye':
        data = conn.recv(1024).decode()
        print(str(data))
        
        message = input('                             -> ')
        conn.send(('-> ' + message).encode())
        
    conn.close()

if __name__ == '__main__':
    server_program()
    input('\nchatting is ended...')