#!/usr/bin/python

import socket
import threading

def tcplink(sock,addr):
	print 'accept new connection from', addr
	sock.send('Welcome')

	while True:
		data = sock.recv(1024)
		if data == 'exit' or not data:
			break
		sock.send('Hello ' + data)
	sock.close()
	print 'Connection from',addr,'closed'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',2345))
s.listen(5)

print 'Waiting for connection'

while True:
	sock,addr = s.accept()
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()