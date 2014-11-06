#!/usr/bin/env python
import sys
import numpy as np

lines = open(sys.argv[1],"r")
outStr = []
nu = 1
for line in lines:
	nu=nu+1
	values = line.partition('#')[0].split()
	if not values: continue
	elif values[0] in ('vp', 'cstype', 'deg', 'bmat', 'step', 'curv', 'curv2', 'surf','parm', 'trim', 'hole', 'scrv', 'sp', 'end', 'con', 'g', 'ng', 'o','bevel', 'c_interp', 'd_interp', 'lod', 'maplib', 'usemap', 'shadow_obj','trace_obj', 'ctech', 'stech'):
		print values
	elif values[0] in outStr: continue
	outStr.append(values[0])
	print "add "+values[0]+ " in list! in line: " +str(nu) 

print "this file contains: " 
for s in outStr:
	print s,
