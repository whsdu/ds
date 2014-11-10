#!/usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib.image as maping
from scipy import ndimage

from PIL import Image

img = maping.imread("./face1_1_0_0.jpg")
gimg = np.dot(img[...,:3],[0.2999,0.587,0.144])

gimg = gimg[::-1]


print np.sum(gimg)

#this part is no damage rotation
zgimg = ndimage.interpolation.zoom(gimg,1.0/2)
zg = Image.fromarray(zgimg)

zrimg = np.asarray(zg.rotate(45))
zr = Image.fromarray(zrimg)
zr.show()

#dzg = image2array(zg)
#print dzg

# np.asarray to real list
# pixels = list(im.getdata())
#width, height = im.size
#pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
# tasks find the boundary and replace

def image2array(im):
    if im.mode not in("L","F"):
        raise ValueError, "ran only convert single-layer images"
    if im.mode =="L":
        a = Numeric.fromstring(im.tostring(),Numeric.UnsignedInt8)
    else:
        a = Numeric.fromstring(im.tostring(),Numeric.Float32)
    
    a.shape = im.size[1],im,size[0]
