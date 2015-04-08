#!/usr/bin/python

import itertools

c = itertools.count(1)

for n in c:
	print n,
	if n > 10: break
print
# count(1) counts from 1 to inifinity

c = itertools.cycle([1,2,3,4,5])
i = 0

for n in c:
	print n,
	i += 1
	if i > 10: break
print

# cycle repeats the list/str anything iterable forever

c = itertools.repeat('Hello',4)

for n in c:
	print n,
print

# print 4 Hello

# we can use takewhile to determine when to exit for the itertools

c = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, c)

for n in ns:
	print n,
print

# takewhile takes a callable object that returns a bool

# chain can conflate 2 iterable object into one 
for c in itertools.chain('ABC','EFG'):
	print c,
print

# groupby() groups the same value in a list together
for key, c in itertools.groupby('AAAABBBBCCCC'):
	print key,list(c),c # c is a itertools.__grouper object

# imap can work on lists of different lenght
r = itertools.imap(lambda x: x*x, itertools.count(1))

r = map(lambda x,y: x*y,[1,2,3],[4,5,6])
print r