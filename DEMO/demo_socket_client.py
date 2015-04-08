#!/usr/bin/python

import socket
from socket import socket,AF_INET,SOCK_STREAM

s = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',2345))
print s.recv(1024)

for name in ['ADAM','MIKE','BUT']:
	s.send(name)
	print s.recv(1024)
s.send('exit')
s.close()
