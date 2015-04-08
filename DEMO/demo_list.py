#!/usr/bin/python

names = ['Michael','Bob','Tracy']
scores = [91,93,94]

print len(names)
print len(scores)

print names[-1:0] # prints nothing because 
				  # slicing does not support reverse access
print names[0:-1]

print names[-1]

# names[3] = 'New' <-- does not work

names.append('New')
print names[-1]

print names.pop() # last element
print names[-1] # New is gone

newname = names.insert(1,scores) # insert list 'score' at underscore 1

print names
print newname # print none, names.insert does not return a list

print names.pop(0)

__l = []

__l.pop()