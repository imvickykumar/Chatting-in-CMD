import cv2
import socket
import pickle
import struct

cap=cv2.VideoCapture(0)
host = input('\nEnter Host IP : ')

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect((host,5000))

while True:

    ret,frame=cap.read()
    c_data = pickle.dumps(frame)
    message_size = struct.pack("L", len(c_data))
    clientsocket.sendall(message_size + c_data)