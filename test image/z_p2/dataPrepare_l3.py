#!/usr/bin/python
import matplotlib.image as maping
from parseFile_l2 import *

def getImageList(sortList):
    imgList = []

    for f in range(len(sortList)):
        img = maping.imread(sortList[f])
        imgList.append(img)

    return imgList


def main():
    direct = sys.argv[1]
    sortList = getSortList(direct)
    imgList = getImageList(sortList)
    
    print len(imgList)
    print len(imgList[0])
    print len(imgList[0][0])

if __name__ == "__main__":
    main()
