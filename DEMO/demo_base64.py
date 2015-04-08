#!/usr/bin/python

import base64
import re

# base64 is a binary encoder decoder package.
# when we open pdf and jpg using texteditor we often see a bunch of 
# random text therefore we need some kind of binary to text device

# to encode, first we read 3 byte of binary
# which is 24 bit, then we take 6 bit and convert it to 4 byte string (each byte is 6 bit)
# then we search for a standard table and convert to the corresponding character

# if we don;t get a perfect fit (the binary code is not divisable by 3) and theres 1 or 2 byte
# leftover we add \x00 after the encoding string and add == on the encoded message

encode = base64.b64encode('Hello World')
# SGVsbG8gV29ybGQ= # encoded message

print encode
print isinstance(encode,str)

decode = base64.b64decode(encode)

print decode
# Hello World

# the encoded message could contain + / or = that could be misunderstood by the web
# so there is a url safe encoder

encode = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print encode


encode = base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print encode

print base64

def urlsafe_encode(s):
	message = base64.urlsafe_b64encode(s)
	return re.sub(r'=','',message)

def urlsafe_decode(s):
	return s + ('=' * (4 - len(s) % 4))

encode = urlsafe_encode('Hello World')
decode = urlsafe_decode(encode)

print encode
print decode

