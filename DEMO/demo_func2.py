#!/usr/bin/python

def calc(*number): # *numbers is a tuple
# 	number[1] = 0 can't do this because tuple inhibit change
	for n in number:
		print n
	return number


n = [10,9,8,7,6]

for i in n:
	print i

print n

l = []
print isinstance(l,(list))

l = 10
print isinstance(l,(list)) # False
print l

calc(1,2,3) 
num = [1,2,3]

calc(*num) # you can call the func with a list by adding a *

def calc(**dic): # this is a dic
	print dic

calc(Hi=99) 

def func2(l):
	print l

func2({'Hi':99,'Ja':88})
