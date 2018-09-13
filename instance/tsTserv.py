#!/usr/bin/python3
from socket import socket
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket()
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock,addr=tcpSerSock.accept()
    print('...connected from:',addr)
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data=data+ctime().encode()
        tcpCliSock.send(data)
#        tcpCliSock.send('[%s]%s'%(ctime().encode(),data))
#tcpCliSock.send('%s'%(data))
    tcpCliSock.close()
tcpSerSock.close()
