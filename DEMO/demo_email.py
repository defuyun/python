#!/usr/bin/python

from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr

import smtplib

msg = MIMEText('Hello, from python','plain','utf-8')
from_addr = '1359198427@qq.com'
password = 'l50451308'

smtp_sever = 'smtp.qq.com'
to_addr = raw_input('To: ')

server = smtplib.SMTP(smtp_sever,25) # create a SMTP server
server.set_debuglevel(1) # now will print commnication detail with the SMTP server
server.login(from_addr,password)

def format_str(s): # encode if contain utf-8 or else cannot be correctly dispalyed
	name,addr = parseaddr(s)
	print 'name:',name,'addr:',addr

	head = Header(name,'utf-8')
	print 'head:',head,'encode:',head.encode()
	print 'addr encode:',addr.encode()

	return formataddr((head.encode(),addr.encode()))

msg['From'] = format_str(u'Yours <%s>' % from_addr)
msg['To'] = format_str(u'Mine <%s>' % to_addr)
msg['Subject'] = Header(u'Hello There').encode()

server.sendmail(from_addr,[to_addr],msg.as_string())