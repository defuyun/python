#!/usr/bin/python

import functools

# paritial func helps us create a partial function with a predetermined parameter

int2 = functools.partial(int,base=2) 
# int is a built in function that converts from str to integer
# the prototype for int is int(var,base = 10)
# in the above code, we create a int2 function that uses int but base 2

print int2('10')

# param of function.partial is defined as (func,*args,**kw)
# so base=2 is passed as dict for **kw
# therefore when we call int2('10') what we did in int('10',**kw) kw = {base:2}

mymax = functools.partial(max,10)

# args = [10]
# mymax(5,6,7) = mymax(args,5,6,7)