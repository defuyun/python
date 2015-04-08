#!/usr/bin/python

class sub(object):
	def __init__(self,*arg):
		self.__list = arg

	def __str__(self):
		return str(self.__list)

mich = sub([1,2,3,4,5])
print mich

print type(mich)([2,4,6,8])

# type(mich) returns an sub type, then we use this type to instantiate 
# another sub object

# actually all classes are created using type

def fn(self,name = 'World'):
	print 'Hello %s' % (name)

Hello = type('Hello',(object,),dict(hello=fn)) # this creates a class Hello

h = Hello()
h.hello()