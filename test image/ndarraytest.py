#!/usr/bin/env python

import numpy as np

dSet = []

matrix1 = [[1,2,3],[3,4,5]]
matrix2 = [[5,4,2],[6,7,8]]

##dSet[0][0].append(matrix1)
##dSet[0][1].append(matrix2)

lSet = []

lSet.append(1)
lSet.append(2)

print lSet

mSet1 = []
mSet1.append(matrix1)
mSet1.append(matrix2)

print mSet1

mSet2 = []
mSet2.append(matrix2)
mSet2.append(matrix1)

print mSet2

dSet.append(mSet1)
dSet.append(mSet2)

print dSet

for m in dSet:
    print m
