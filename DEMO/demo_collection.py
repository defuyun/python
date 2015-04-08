#!/usr/bin/python

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# namedtuple is used to create a tuple that looks like a class to we know what
# the elements are for 

Point = namedtuple('Point',['x','y']) # namedtuple creates a tuple that has limited element and gives each element a corresponding name
p = Point(1,2)

print p.x,p.y
print isinstance(p,tuple) # true, p is still a tuple

# deque is a double linked list, it's better than list when it comes in insertion

q = deque([1,2,3,4])
q.append(1)
print q

q.appendleft(2)

print q
print q[2]
print isinstance(deque,list)
# deque behaves similar to list but has appendleft and popleft

# default dict allows us to define a dfault return value if the key does not exist

d = defaultdict(lambda: 'N/A') # the default value must be passed by callable object e.g. function
print d[1]
print isinstance(d,dict)

# counter is a dict that is used as a counterr
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print c
print isinstance(c,dict)
