#!/usr/bin/env python

import numpy as np
from PIL import Image

im = Image.open("face1_1_0_0.jpg")

aim = np.asarray(im.rotate(45))

s = Image.fromarray(aim)
s.show()

print len(aim)
