#!/usr/bin/python

import types

# we can find the type of vars with the type function
# type returns a type type

print type(12) # <type 'int'>
print type('str') # <type 'str'>

print isinstance(10,type(12)) # true

print type(int) # <type 'type'>

def func():
	pass

print type(func) # <type 'function'>

# type contains predetermined type members to make things easier when comparing

print type('str') == types.StringType # in types package
print type(12) == types.IntType

# the dir function lists all the component of an object

print dir(int) # you see __abs__ and abs, __abs__ is a private funct and when you call abs, it then calls __abs__

# there are some other function to get attribute from an object
class MyObject(object):
	def __init__(self,name,other):
		self.__name = name
		self.__other = other

	def get_name(self):
		return self.__name

	def get_other(self):
		return self.__other	

obj = MyObject('Barch','Other')
obj.get_name()

print dir(obj)

# hasattr can be used to see if there is such attribute

print hasattr(obj,'name') # False
print hasattr(obj,'__name') # False
print hasattr(obj,'_MyObject__name') # True

# hasattr is usually used with getattr

if hasattr(obj,'get_name'):
	f = getattr(obj,'get_name') # if 'get_name' does not exist, throws AtributeError
	print f()

# setattr creates an attribute
if not hasattr(obj,'say_hello'):
	setattr(obj,'say_hello', lambda: "Hello World")
	print obj.say_hello()