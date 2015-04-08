#!/usr/bin/python

d = {'Hi':'Cat','Bye':'12'}

for k,v in d.iteritems(): 
	print "key: %5s, value: %5s" % (k,v)

for r in d.iteritems(): # iteritem returns 2 values(a tuple): key and value
	print r

for i, v in enumerate(['A','B','C']): # enumerate is similar to iteritems but return index and value
	print i, " ", v

for x,y in [(1,1),(2,2),(3,3)]:
	print x,y

# what this does is first 'in' goes through each of the tuple
# and each of the tuple then assign value to both x and y
# e.g if we did x,y = (1,1) then x = 1 and y = 1, 'in' just does
# the iteration

# List Comprehension is a list creator
print [x*x for x in range(1,11) if x % 2 == 0]

print [x for x in range(1,11,2)]

print [m + n for m in 'ABC' for n in 'XYZ'] # nested loop
"""
	for m in 'ABC':
		for n in 'XYZ':
			m + n

"""
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


print [k.lower() + ' = ' + v.lower() for k, v in d.iteritems() if isinstance(k,str) and isinstance(v,str)]
# lower case k + (+ with string means append to) lower case v
