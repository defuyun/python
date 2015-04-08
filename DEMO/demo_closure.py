#!/usr/bin/python

def count():
	fs = [] 
	for i in range(1,4):
		def sqr():
			return i*i
		fs.append(sqr) # here the sqr function is pushed in fs
	return fs # fs returned with 3 sqr functions [sqr,sqr,sqr]

f1,f2,f3 = count() # each of f1,f2,f3 gets a sqr function

print f1(),f2(),f3() # 9 9 9 
# the answer is not  1 4 9 because sqr function is only ran when
# f1,f2,f3 calls it, it wasn't ran when count was called.
# when f1,f2,f3 calls it, i after incrementing through 1,2,3 in the count
# function is 3 so sqr returns 3*3

# a way of getting through this is defining another function inside the sqr func

def count2():
	fs = []
	for i in range(1,4):
		def sqr(j): # pass in j which is then taken by realsqr
			def realsqr():
				return j * j
			return realsqr
		fs.append(sqr(i)) # return realsqr but param is i
	return fs
