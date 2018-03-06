# Echo server
import socket
import os
from time import ctime

HOST = ''
PORT = 50007


def listdir():
    return os.listdir(os.curdir)


def name():
    return os.name


commands = {'date': ctime, 'os': name, 'ls': listdir }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)
    while True:
        conn, addr = serverSocket.accept()
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if data in commands:
            answer = commands[data]()
        else:
            answer = 'Error command'
        conn.sendall(repr(answer).encode('utf-8'))

