#!/usr/bin/python
import matplotlib.image as maping
from parseFile_l2 import *
from PIL import Image

def getImageList(sortList):
    imgList = []

    for f in range(len(sortList)):
        imgArr = maping.imread(sortList[f])
        imgList.append(imgArr)

    return imgList

def array2Img(array):
    return Image.fromarray(array)

def main():
    direct = sys.argv[1]
    sortList = getSortList(direct)
    imgList = getImageList(sortList)
    
    print len(imgList)
    print len(imgList[0])
    print len(imgList[0][0])

    img = array2Img(imgList[0])
    img.show()

if __name__ == "__main__":
    main()
