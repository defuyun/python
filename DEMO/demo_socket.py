#!/usr/bin/python

import socket

# TCP/IP
# the IP is responsible for transmitting data by splitting the data into small ip
# packages and sending them through the modem 
# an IP package contains source ip address, port and target ip address and port

# TCP is responsible for making sure that the data is sent

# a port is reponsible for determining which process responds to the call
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80)) # 80 is standard port for web

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buff = []

while True:
	d = s.recv(1024)
	if d:
		buff.append(d)
	else:
		break

s.close()
data = ' '.join(buff)

header, html = data.split('\r\n\r\n', 1)
print header