#!/usr/bin/python

# the difference between creating a generator and a list comprehension is [] and ()
# when using a list comprehension, a whole list is created and this costs a large amount 
# of space

# a generator stores an algorithm that computes the next ouput in the loop
# so it costs less space

g = (x * x for x in range(1,11,2)) # g is a generator

print g # <generator object <genexpr> at 0x10bedaaa0>

print g.next()

# generator is iterable
for n in g:
	print n,
print

def fib(n):
	x,y = 0,1
	i = 0
	while i < n:
		yield y
		i += 1
		x,y = y,x+y # x = y and y = x+y are concurrent so x retains it's old value when computing x + y 
		# it's actually a tuple y,x+y


for i in fib(6):
	print i,
print

def demo():
	print 'step 1'
	yield # equivalent to return None
	print 'step 2'
	yield # each next runs up to a yield
	print 'step 3'
	yield
#	return 10  # generator cannot contain return

d = demo()
print d.next() 
""" 
	prints:
		step 1
		None

"""
# demo runs print step 1 then yield(return) None so the return value is None which is printed
# when gen ends it throws StopIteration
