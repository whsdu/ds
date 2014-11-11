#!/usr/bin/env python
from parseFile_l2 import *
from dataPrepare_l3 import *


def getRotateImg(img,degree):
    rimg = img.rotate(degree)
    return rimg

def getImgSize(img):
    return img.size

def main():
     direct = sys.argv[1]
     sortList = getSortList(direct)
     imgList = getImageList(sortList)
     img = array2Img(imgList[0])
     rimg = getRotateImg(img,45)
     print rimg
     rimg.show()


if __name__ == "__main__":
    main()
