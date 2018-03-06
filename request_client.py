# Echo client
import socket

HOST = 'localhost'
PORT = 50007
req = input()

while req:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(req.encode('utf-8'))
        data = s.recv(1024)
        print('Received', data.decode('utf-8'))
        req = input()