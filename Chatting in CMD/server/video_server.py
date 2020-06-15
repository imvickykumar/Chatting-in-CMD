import pickle
import socket
import struct
import cv2

host_name = socket.gethostname()
HOST = socket.gethostbyname(host_name)
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

print('\nHost IP is : ', HOST)
print('\nWaiting for receiver...\n')
    
conn, addr = s.accept()
data = b''
payload_size = struct.calcsize("L")

while cv2.waitKey(33) != 27:
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)