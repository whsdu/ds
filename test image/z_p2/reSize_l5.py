#!/usr/bin/env python

from rotate_l4 import *
from dataPrepare_l3 import *
from parseFile_l2 import *

def getResizeImg(img,size):
    size = [int(round(s)) for s in size]
    img.thumbnail(size,Image.ANTIALIAS)
    return img

def getTransImg(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] ==0 and item[2] ==0:
            newData.append((255,255,255,0))
        else:
            newData.append(item)

    img.putdata(newData)

    return img


def main():

    direct = sys.argv[1]
    
    #level 2
    sortList = getSortList(direct)
    
    #level 3
    imgList = getImageList(sortList)
    
    img = array2Img(imgList[0])

    # level 4
    degree = 45
    imgSize = getImgSize(img)

    rimg = getRotateImg(img,degree)

    # level 5
    resizeRatio = 2
    width,height = imgSize
    resize = [width/resizeRatio,height/resizeRatio]

    rsimg = getResizeImg(rimg,resize)
    
    print rsimg
#    rsimg.show()
    timg = getTransImg(rsimg)
    
    timg.show()


if __name__ == "__main__":
    main()
