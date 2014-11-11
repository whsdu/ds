#!/usr/bin/env python

import h5py
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as maping

from scipy import ndimage
from PIL import Image

f = h5py.File("testSet",'r')
dset = f["set1"]
# needs modification to read dataset

img = Image.fromarray(dset)
img.show()

