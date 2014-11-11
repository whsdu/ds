#!usr/bin/env python

import matplotlib.image as maping
from scipy import ndimage
from PIL import Image

import numpy as np
import scipy as sp
import sys
import h5py

def loadImage(filename):
    d_img = maping.imread(filename)
    return d_img

def transImg(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
#    img.save("img2.png", "PNG")
    return img

def converD2A(d_img):
    return Image.fromarray(d_img)


def rotate(img):
    rimg = img.rotate(45)
    return rimg

def zoomImage(d_img):
    d_zimg = ndimage.interpolation.zoom(d_img,1.0/2)
    return d_zimg
def imageResize(img,size):
    size = [int(round(s)) for s in size]
    img.thumbnail(size,Image.ANTIALIAS)
    return img


def getWhiteBackground():
    wb = np.ones((600,600))
    wb = wb*255
    return wb
def getImagePixels(im):
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    return pixels


def main():
    resizeRatio = 4



    d_img = loadImage(sys.argv[1])
    img = converD2A(d_img)

    #set the resize value
    width,height =  img.size
    resize = [width/resizeRatio,height/resizeRatio]
    
    #rotation use Image
    img = rotate(img)
    
    #resize use Image
    img = imageResize(img,resize)

    #transparent this image for position and background variance
    img = transImg(img)

    #white background
    background = getWhiteBackground()
    bg_img = converD2A(background)

    #need a function to calculate the range of postion 
    #call function to calculate postion range
    #end

    #position and background variance generate
    bg_img.paste(img,(50,50),img)

    # bg_img is a gray image with given size set as background
    bg_img.show()
    pixels = getImagePixels(bg_img)
    
    print str(len(pixels)) + "..." + str(len(pixels[0]))+"..." 

    print "pixels is a list: " +str(isinstance(pixels,list))
    print "pixels row is a list: " + str(isinstance(pixels[0],list))
    print "pixels cell is a list: " + str(isinstance(pixels[0][0],list))

#    f = h5py.File("testSet")
#    f.create_dataset("set1",data=pixels)

if __name__ == "__main__":
    main()

