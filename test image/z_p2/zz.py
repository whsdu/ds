#!/usr/bin/env python
from position_l6 import *
from reSize_l5 import *
from rotate_l4 import *
from dataPrepare_l3 import *
from parseFile_l2 import *
from background_l0 import *

import numpy as np

def getDegreeList(degree):
    degreeList = range(0,360,degree)
    return degreeList

def getResizeRange(longth):
    resizeList = np.arange(1.5,4.5,longth)
    return resizeList

def getWhiteImg(wb_hight,wb_width):
    wb = getWhiteBackground(wb_hight,wb_width)
    wbimg = array2Img(wb)
    return wbimg

def main():
    direct = sys.argv[1]
    degreeList = getDegreeList(5)
    resizeRange = getResizeRange(0.5)
    
    wb_hight,wb_width = 600,600
    bg_size = [wb_width,wb_hight]

    #level 2
    sortList = getSortList(direct)
    
    #level 3
    imgList = getImageList(sortList)
    
    dSet = []
    for image in imgList:
        img = array2Img(image)

        #Level 4 pose variance: x axis rotation
        # get image size for Level 5: resize
        imgSize = getImgSize(img)

        rotation_index = []
        for degree in degreeList:
            rimg = getRotateImg(img,degree)
            
            width,height = imgSize

            #Level 5 size variance: resize to small image
            size_index=[]
            for resizeRatio in resizeRange:
                resize = [width/resizeRatio,height/resizeRatio]   
                rsimg = getResizeImg(rimg,resize)
                
                # conver to transparent
                timg = getTransImg(rsimg)
                position_list = getBoundary(bg_size,timg.size)
                w_list,h_list = position_list

                #Leve 6 postion variance: along width
                w_index = []
                for w in w_list:
                    h_index = []
                    for h in h_list:
                        wb_img = getWhiteImg(wb_hight,wb_width)
                        p_img = getPositionImg(wb_img,timg,w,h)
                        
                        d_img = img2Array(p_img)
                        h_index.append(d_img)
                    
                    w_index.append(h_index)
                
                size_index.append(w_index)

            rotation_index.append(size_index)
        
        dSet.append(rotation_index)

    print " hope I can see this line !"


if __name__ == "__main__":
    main()
