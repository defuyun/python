#!/usr/bin/python

import math

i = 10

print isinstance(i,(float))

def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny # python can return multiple values, but these values are actually passed as tuple

x,y = move(100,100,60,math.pi/6) # equivalent to x,y = (nx,ny)
print x,y 

def append(L=[]):
	L.append('END')
	return L

def change(i):
	i = 10
	print i
	return i

l = [1,2,3]
append(l)
print l

change(l)
print l

print append()
print append() # prints END twice
# L = [], [] is a defined memmory location, when first called,
# L = [] appends 'END', when it is called again, another 'END'
# is appended at the end