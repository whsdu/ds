#!/usr/bin/env python
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as maping
import numpy as np
import scipy as sp
from scipy import ndimage
import glob,os
from PIL import Image

def r2g(rgb):
    img = np.dot(rgb[...,:3],[0.2999,0.587,0.144])
    return img[::-1]

def showImage(img):
    plt.imshow(img,cmap=plt.get_cmap('gray'))
    plt.show()


##dset = []
#for infile in glob.glob("./face_0/*.jpg"):
#    img = maping.imread(infile)
 #   gImg = r2g(img)
  #  dset.append(gImg)

#for image in dset:
#    showImage(image)


def parseFile(direct):
    
    fileNum = len(glob.glob(direct))
    waitList = range(fileNum)

    for infiel in glob.glob(direct):
        string = infiel.split("_")
        waitList[int(string[3])]=infiel
        print string[2] + " and "+string[3]
    print "the total number of file is: "+ str(fileNum)

    for f in waitList:
        print f

    return waitList

def convertImage(waitList):
    dset = []
    for f in range(len(waitList)):
        img = maping.imread(waitList[f])
        gImg = r2g(img)
        dset.append(gImg)

    return dset

def simpleRotate(ndArray,degree):
    rotate = ndimage.rotate(ndArray,degree)
    showImage(rotate)

#def simpleRescale(image,


def testWaitList():
    waitList = parseFile("./face_0/*.jpg")
    dset = convertImage(waitList)
#    for image in dset:
#        showImage(image)
    print "main function finished!"
    print len(dset)
    ndarr = np.array(dset)

    return dset

def main():
    dset = testWaitList()
    simpleRotate(dset[0],30)

if __name__ == "__main__":
    main()
    
