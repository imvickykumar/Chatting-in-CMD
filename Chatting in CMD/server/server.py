import socket, datetime, os

day = str(datetime.datetime.now()) + ' [ NEW ]!@#' + '...'

def history(host):

    server = host + 's_server.txt'
    client = host + 's_client.txt'

    with open(server, 'a') as s:
        s.write(day)
            
    with open(client, 'a') as c:
        c.write(day)
    
    with open(server, 'r') as s:
        res = s.read()
    
    with open(client, 'r') as c:
        rec = c.read()
        
    for s, c in zip(res.split('!@#'), rec.split('!@#')):
        print(c)
        print('                                                            ' + s)
        
    return server, client

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
    server, client = history(host)
    message, j = 'hi', 5
    
    while message.lower().strip() != 'bye':
    
        os.system('color ' + str(j))
        j = (j + 1) % 7
        
        data = conn.recv(1024).decode()
        
        with open(client, 'a') as c:
            c.write(data + '!@#')
        
        print(data)
        message = input('                                                            -> ')
        
        with open(server, 'a') as s:
            s.write(message + '!@#')
    
        conn.send((' ' + message).encode())
    conn.close()

if __name__ == '__main__':    
    server_program()
    input('\nchatting is ended...')