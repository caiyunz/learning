#!/usr/bin/python3
from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input('> ')
    data=data.encode()
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR=udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)
udpCliSock.close()
