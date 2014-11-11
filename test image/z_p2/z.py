#!/usr/bin/env python

#1. import package
import matplotlib.image as maping
import numpy as np
import scipy as sp
import sys
import h5py

from scipy import ndimage
from PIL import Image

#2. get the waitlist
#pass waitlist
#get return dSet3 from 3 --> fill the h5py dataset

#3. get the first one in wait list --> end1
#pass d_image to 4 for each one
#get return dSet 4 --> add to dset3 --> until complete waitlist

#4. rotate Y axis startpoint --> end
# get img from 3 rotate 0 --> end pass to 5 for each one
# get return dSet5 --> added to dSet4 --> return to 3, once complete end

#5. resize from ratio 2 --> 4
# get img from 4 resize 2-->4  pass to 6 for each one
#get return dSet6 --> construct dSet5 --> return to 4,once complete end

#6. position rearrange along width 0-->end (white background)
# get img from 5 rearrange position along width 0 --> end and pass to 7 for each one
# get return dset7 from 7 --> construct dSet6--> once comple end ,return to 5


#7. position rearrange along height 0-->end (white background)
# get img from 6, pass to actuall function **(iterate over 0 -->end)
# get return dSet from actural function--> construct dSet7 --> return to 6
