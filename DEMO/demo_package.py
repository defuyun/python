#!/usr/bin/python

# import demo_gen # runs demo_gen
import sys

# package must contain __init__.py file or else python treates it as an normal folder

' This is a demo package ' # python treats the first string in a package file as the file description

__author__ = 'Me'

def test():
	args = sys.argv
	if len(args)==1:
		print "Hello World"
	elif len(args) == 2:
		print "Hello",args[1]
	else:
		print "Too many args"

if __name__ == '__main__': # would only run if it's not imported by other files
	test()

print __name__ # prints main if ran by itself and demo_package if ran by other file

# when importing, we can use alias, for example python has cStringIO and StringIO
# we can try to import a package as another package

try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

try:
	import json
except ImportError:
	import simplejson as json

# simple variables in python are public scoped(can be used every in the function)
# if we want a private scope we write _ or __ in front but this does not limit access
# it's just telling the user that this is private

_list = [1,2,3,4]

def func():
	print _list # this can be accessed
	
func()
