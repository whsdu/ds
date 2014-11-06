#!/usr/bin/env python

from PIL import Image

im = Image.open("face1_1_0_0.jpg")
im.rotate(45).save("rotate.jpg","JPEG")
