#!/usr/bin/env python
import numpy  as np
import h5py

dSet = []
loop1 = range(10)
loop2 = range(10)
loop3 = range(100)

dIndexSet = np.ones((len(loop1),len(loop2),len(loop3)),dtype=np.int)

list = []
for l in loop1:
    for n in loop2:
        for m in loop3:
            list.append([l,n,m])

f = h5py.File("nt.hdf5")
dSet = f.create_dataset("dSet",shape = (len(list),600,600))


print len(list)
for t in range(101):
    print list[t]

i = 0
for l in list:
    matrix = np.ones((600,600))
    matrix = l[2]*matrix
    
    dSet[i]=matrix
    i = i+1
    
    if i%10 == 0:
        f.flush()
        print "has flush: "+ str(i) + "matrixs"

print len(dIndexSet)
print len(dIndexSet[0])
print len(dIndexSet[0][0])
