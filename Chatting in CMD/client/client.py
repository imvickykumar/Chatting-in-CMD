import socket, datetime, os

day = str(datetime.datetime.now()) + ' [ NEW ]!@#' + '...'

def history(host):

    server = host + 'c_server.txt'
    client = host + 'c_client.txt'

    with open(server, 'a') as s:
        s.write(day)
            
    with open(client, 'a') as c:
        c.write(day)
    
    with open(server, 'r') as s:
        res = s.read()
    
    with open(client, 'r') as c:
        rec = c.read()
        
    for s, c in zip(res.split('!@#'), rec.split('!@#')):
        print(s)
        print('                                                            ' + c)
        
    return server, client

def client_program():
    host = input('\nEnter host IP : ')
    
    # host = '192.168.56.1'
    port = 5000

    nick = input('\nEnter your Nickname : ')
    # nick = 'vicks'
    
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print('\nConnected...\n')
    server, client = history(host)

    message, j = "hi, it's " + nick, 1

    while message.lower().strip() != 'bye':
    
        os.system('color ' + str(j))
        j = (j + 1) % 7

        client_socket.send((' ' + message).encode())
        data = client_socket.recv(1024).decode()
        
        with open(server, 'a') as s:
            s.write(data + '!@#')

        print(data)
        message = input("                                                            -> ")
        
        with open(client, 'a') as c:
            c.write(message + '!@#')

    client_socket.close()
    
if __name__ == '__main__':
    client_program()
    input('\nchatting is ended...')