#!/usr/bin/python

class student(object):
	pass

one = student()

print one

# you can define class member for class in python
# unlike c++ the members does not have to be defined in the class definition

one.name = "Barch"
one.age = 12

print one.name, one.age

class stud2(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

# when class is instantiated, it calls the init function
# self is passed in by defualt, equivalent to this pointer in c++

one = stud2("Name",12)

# the __ in name and score makes them private variables 

# print one.__name,one.__score # does not work because stud2 does not name 
# the variable __name, __score as you specified but rather _stud2__name

print one._stud2__name

#inherit

class stud3(stud2):
	def run(self):
		print self.get_name(), "is running" # we need get_name because __name is protected, the relation between child and parent is similar to c++

Barch = stud3('Barch',12) # Barch inherits stud2 and __init__ of stud2 is ran for instantiation

Barch.run() 