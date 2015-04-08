#!/usr/bin/python

import logging # logging.
logging.basicConfig(level=logging.INFO)

try:
	print 'try...'
	r = 10/0
	print 'result:',r
except ZeroDivisionError, e:
	print 'except:',e
finally:
	print 'finally...'

print 'END'


def divide(a,b):
	return a/b

a = 10
b = '0'
r = None
try:
	r = divide(a,b)
except TypeError:
	try:
		r = divide(int(a),int(b))
	except ZeroDivisionError:
		r = divide(int(a),int(b) + 1)
except ZeroDivisionError:
	r = divide(a,b + 1)
finally:
	print r

# you can catch exception from functions
# if no one catches it, python interpolator will
# and prints it on the screen

# if we don't want to catch the error and let the program continue running
# after an error occured we can use logging

try:
	divide(10,0)
except ZeroDivisionError, e:
	logging.exception(e)

print 'keep runnig'

# others uses of logging include info, error etc

logging.info('Hi') # INFO:root:Hi
