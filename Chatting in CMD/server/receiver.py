import socket
import os, tqdm

host_name = socket.gethostname()
SERVER_HOST = socket.gethostbyname(host_name)

print('\nHost IP is : ', SERVER_HOST)
print('\nWaiting for receiver...\n')

SERVER_PORT = 5001
BUFFER_SIZE = 4096 # 4KB
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
client_socket, address = s.accept()

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    for _ in progress:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)

client_socket.close()
s.close()