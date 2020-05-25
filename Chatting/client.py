import socket

def client_program():

    host = input('\nEnter Host IP : ')
    port = 5000

    nick = input('\nEnter your Nickname : ')
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print('\nConnected...\n')
    message = "hi, it's " + nick

    while message.lower().strip() != 'bye':

        client_socket.send(('-> ' + message).encode())
        data = client_socket.recv(1024).decode()

        print(str(data))
        message = input("                             -> ")

    client_socket.close()
    
if __name__ == '__main__':
    client_program()
    input('\nchatting is ended...')
