import socket

PORT = 80
site = input('Enter site addr: ')
if not site:
    site = 'google.com'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsock:
    clientsock.connect((site, PORT))
    clientsock.sendall("GET /\n".encode('utf-8'))
    ans = clientsock.recv(1025)
    while ans:
        print(ans.decode('utf-8'))
        ans = clientsock.recv(1025)

