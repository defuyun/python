#!/usr/bin/python

# python has a struct package that converts from int to string 
import struct

print struct.pack('>I',1256)

# '>' means read as big-endian and I means convert from integer

print struct.unpack('>IH','Hello ')

# I is convert to integer, H is convert to short
