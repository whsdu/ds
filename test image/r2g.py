#!/usr/bin/env python
import matplotlib.image as mping
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    img = np.dot(rgb[...,:3],[0.2999,0.587,0.144])
    return img[::-1]

img = mping.imread('face1_1_0_0.jpg')
print img.shape
gray = rgb2gray(img)
print len(gray.shape)
print gray.shape
plt.imshow(gray,cmap=plt.get_cmap('gray'))
plt.show()
