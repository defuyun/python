#!/usr/bin/python

demo = {}

print demo
print demo.get('Thomas','Not here') # check if Thomas exists, if not return 'Not here'

demo['Thomas'] = 95

print demo.get('Thomas','Not here') # return the value 95
print demo['Thomas'] # use above because this one gives error

if 'Thomas' in demo: 
	print demo['Thomas']

print 'Thomas' in demo

i = 'String'

demo[i] = 'Hi'

print demo

# demo.pop('Hi') gives error if no key
demo.pop('Thomas')
print demo

s = set([(1,[2,3]),1]) # unhashable list, hash values must be constant

print s