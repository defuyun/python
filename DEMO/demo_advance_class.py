#!/usr/bin/python

class stud(object):
	pass
	def set_name(self,name):
		self.__name = name

	def get_age(self):
		return self.__age


mich = stud()
mich.__name = 'Michael' # the self defined name is not a private var like __name

mich.set_name('Bob') # bob is defined in the class so it's private

print mich.__name
print mich._stud__name

def set_age(self,age):
	self.__age = age

from types import MethodType
mich.set_age = MethodType(set_age,mich,stud) # we give mich a member function called set_age
# but remember that this function is only linked to mich but it's not really a member funciton
# the __age var is not converted to the private _stud__age
mich.set_age(25)

print mich.__age

james = stud()
# james.set_age(10) # does not work

# if we want to give all stud objects the set_age function then we write
stud.set_age = MethodType(set_age,None,stud)
james.set_age(10)

print james.__age

# if we want to limit the vars available to a function we use __slots__

class stud(object):
	__slots__ = ('__name','__age')

	def __init__(self,name,age):
		self.__name = name
		self.__age = age

mich = stud('James',12)
# mich.__score = 0 # AttributeError

class stud2(stud):
	__slots__ = ('__score')

	def set_score(self,score):
		self.__score = score

# the child inherits it's parent's slot + it's own slot
mich = stud2('James',12)
mich._stud2__score = 0

print mich._stud__name,mich._stud__age,mich._stud2__score
# name and age is in stud so we use stud instead of stud2


# a way to simpilify the usage of setter(set_score) and getter (get_score) is the 
# use of @property 
# @property is a built-in decorator that python defined for us, it creates a getter
# and setter decorator
"""
	def foo():
	    doc = "The foo property."
	    def fget(self):
	        return self._foo
	    def fset(self, value):
	        self._foo = value
	    def fdel(self):
	        del self._foo
	    return locals()
	foo = property(**foo())

"""

class stud(object):
	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self,score):
		self.__score = score 

mich = stud()
mich.score = 12

print mich.score

# when we use property it creates a getter function and a corresponding setter function
# beware that we must define property before defining the setter, because the setter
# is created by property
