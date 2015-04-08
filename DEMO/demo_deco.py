#!/usr/bin/python

import time
import functools
# functions are also objects so they can be assigned

def ftime():
	print time.strftime('%H:%M:%S')

func = ftime

func()

# functions have an attribute __name__

print func.__name__

# a decorator is a Higher Order function (map,reduce) that returns a function
# you can use it when you want to add features to an existing function but don't
# make modifications

def log(func):
	def wrapper(*args,**kw):
		print func.__name__
		return func(*args,**kw)
	return wrapper

@log # equivalent to ttime = log(ttime) log returns the function wrapper
def ttime():
	print time.strftime('%H:%M:%S')

# wrapper takes the argument of ttime
# prints the function's name then runs
# the passed in function and return func's
# return value

ttime() 

# if decorator needs args then we need to wrap it up like we did in the sqr func

def log(text):
	def deco(func):
		def wrapper(*args,**kw):
			print text,func.__name__
			return func(*args,**kw)
		return wrapper
	return deco

# tttime = log('runs')(ttime)
@log('runs') 
# log('runs') runs the function log which contains the decorator
# it returns the decorator and then the decorator calls tttime
# the proceeding predure it the same as above

def tttime():
	print time.strftime('%H:%M:%S')

tttime()

print tttime.__name__ # wrapper because the when we use the decorator, the wrapper function
# is returned which overlaid tttime

# python provides a function that does wrapper.__name__ = func.__name__ in functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'this uses wrap',func.__name__
		return func(*args,**kw)
	return wrapper

@log
def ttttime():
	print time.strftime('%H:%M:%S')

print ttttime.__name__

def tlog(textorfunc):	
	if not isinstance(textorfunc,str):
		@functools.wraps(textorfunc)
		def wrapper(*args,**kw):
			print "====== begin call ======"
			i = textorfunc(*args,**kw)
			print "====== end call ========"
			return i
		return wrapper

	else:
		def deco(func):
			print textorfunc
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print "====== begin call ======"
				i = func(*args,**kw)
				print "====== end call ========"
				return i
			return wrapper	
		return deco

@tlog('run')
def f():
	pass

@tlog
def f1():
	pass

f()
f1()