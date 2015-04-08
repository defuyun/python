#!/usr/bin/python

import os
import re
import json

with open('demo_file.py','r') as f: # equivalent to try: open .... finally and automatically closes the file

#	print f.read()

	# f.read() reads the whole file, if it's a very big file than the pc may crash
	# we can use read(size) to limit the amount read each time

	print f.read(10) # reads 10 char

	for line in f.readlines():
		print line.strip() # removes '\n'  

# prints operating sys
print os.name

# prints detail
print os.uname()

# prints environment as dict
print os.environ

# get a environ variable
print os.getenv('PATH')

# looks at the absolute PATH
print os.path.abspath('.') # /Users/tianqiliu/Documents/python/DEMO

# join 2 paths
print os.path.join(os.path.abspath('.'),'test')

# mkdir
os.mkdir(os.path.join('.','test'))

# rm -r
os.rmdir(os.path.join('.','test'))

# split the path
print os.path.split(os.path.abspath('.'))

# split the file and it's suffix
print os.path.splitext('demo_file.py')

# python does not provide a copyfile funciton 
# because copy file is not a faculty of the operating system
# therefore theres no port

def search(s,fs='.'):
	for _f in os.listdir(fs):
		if os.path.isdir(_f):
			search(s,os.path.join(s,_f))
		else:
			if re.match(r'^.*%s.*$' % s,_f):
				print _f

search('list')

#Json can be read by any language because it's a str variable
d = dict(name='bob',age=20,score=88)

print json.dumps(d)