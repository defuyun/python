#!/usr/bin/python

import __builtin__

print abs 
#<built-in function abs> returns the actual function

x = abs(-10)
# functions are also variables, they can be replaced

print x

abs = 10

print abs # 10
# this doesn't really overlay abs because abs is alias for __builtin__.abs

l = [-10,1,-9,2,-8]
abs = __builtin__.abs

print map(abs,l) # equivalent to c++ for_each(iter,iter,func) except iter is replaced with an actual list

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def sum3(x,y,z):
	return x + y + z

# print reduce(sum3,l) # reduce only works with 2 argument

# valid names
print map(lambda s: s[0].upper() +  s[1:].lower(),['adam', 'LISA', 'barT'])

#product of list
def prod(*l):
	return reduce(lambda x,y: x*y, l)

l = [1,2,3,4]

print prod(*l) # 24

# filter forms a list according to bool return value
def not_prime(n):
	for i in range(2,n/2+1): # n/2+1 because 4/2 = 2 , 2 to 1 does not exist
		if n % i == 0:
			return False
	return True

print filter(not_prime,range(101))

# sorted by default is ascending order
print sorted([36,5,12,9,21]) # [5, 9, 12, 21, 36]

#to make a descinding sort you need your own func
def reverse(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	return 0

print sorted([36,5,12,9,21],reverse) # [5, 9, 12, 21, 36]
