#!/usr/bin/python3
from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=10240
ADDR=(HOST,PORT)

tcpCliSock=socket()
tcpCliSock.connect(ADDR)
while True:
    data=input('> ')
    data=data.encode()
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcpCliSock.close()
