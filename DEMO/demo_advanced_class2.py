#!/usr/bin/python

# the __str__ attribute corresponds to the print statement
# similar to overloading the ostream << in c++

class stud(object):
	__slots__ = ('__name','__score')
	@property
	def name(self):
		return self.__name

	@property 
	def score(self):
		return self.__score

	@score.setter
	def score(self,score):
		self.__score = score

	@name.setter
	def name(self,name):
		self.__name = name


	def __str__(self):
		return self.__name + ' ' + str(self.__score)

mich = stud()
mich.name = 'Mich'
mich.score = 10

print mich

# the __iter__ attibute allows the object to be iterated in the for...in... loop
# the __iter__ returns an iterator object which will then call the next method
# defined for the object when it's being iterated

class fib(object):
	def __init__(self):
		self.__a = 0
		self.__b = 1

	def __iter__(self):
		return self

	def next(self):
		if self.__a > 100:
			raise StopIteration()

		self.__a,self.__b = self.__b,self.__a+self.__b
		return self.__a

f = fib()

for i in f:
	print i,
print

# when f enters the for loop, for calls the __iter__ function,
# the funct returns the fib object (fib is the iterator because it contains the next method)
# any object with a next method is an iterator
# the loop keeps on calling next and giving it to i


# the __getitem__ attribute allows the object ot behave like a list, similar to overloading
# [] in c++

class fib2(fib):
	def __getitem__(self,n):
		a,b = 0,1
		for x in range(n):
			a,b = b,a+b
		return n,b

f2 = fib2()

print f2[1],f2[3],f2[5]

# there are other attribute such as __setitem__ and __delitem__ which can be used to simulate
# a list

# __getattr__ is used when we ask to get an attribute that does not exist in the object

class fib3(fib2):
	def __getattr__(self,attr):
		if attr == 'n':
			return 10
		raise AttributeError('%s cannot be found' % (attr)) # remember to raise error because by default 
		# getattr returns None, so when we ask for a non-existing attribute and python calls __gettattr
		# after going through the various if statement it exits with a None, which is bad because
		# we didn't find a match and no error was raised

f3 = fib3()
print f3.n
# print f3.r # without raise, it prints None

# using __getattr__ to create a dynamic API link

class chain(object):
	def __init__(self,path=''):
		self.path = path

	def __getattr__(self,path):
		return chain(self.path + '/' + path)

	def __str__(self):
		return self.path

	def user(self,name):
		return chain(self.path + '/' + name)

print chain().hello.world.api
# /hello/world/api

# so what happened is, we ask for attribute hello, which does not exist
# so if calls __getattr__ which returns a chain object with path = '/hello'
# then this object calls world which is also not there (recursion occurs)

print chain().user('Micha').home.download.AVI

# __call__ is called when we do instance(arg)

class stud(object):
	def __init__(self,name):
		self.__name = name

	def __call__(self):
		print self.__name

stud('name')() # prints name

# the callable funciotn can be used t osee if an object is callable

print callable(stud) 