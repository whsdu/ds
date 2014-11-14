#!/usr/bin/env python
from position_l6 import *
from reSize_l5 import *
from rotate_l4 import *
from dataPrepare_l3 import *
from parseFile_l2 import *
from background_l0 import *

import numpy as np
import h5py
import time

def getDegreeList(degree):
    degreeList = range(0,360,degree)
    return degreeList

def getResizeRange(lower,upper,scale):
    resizeList = np.arange(lower,upper,scale)
    return resizeList

def getWhiteImg(wb_hight,wb_width):
    wb = getWhiteBackground(wb_hight,wb_width)
    wbimg = array2Img(wb)
    return wbimg
def getOperationIndexList(list1,list2,list3):
    operationIndexList = []
    for l in list1:
        for n in list2:
            for m in list3:
                operationIndexList.append([l,n,m])
    return operationIndexList

def getPositionCor(resizeRange,bg_size,o_img_size,shift):
    o_img_w,o_img_h = o_img_size
    
    resizeDic = {}
    for resizeRatio in resizeRange:
        resize = [o_img_w/resizeRatio,o_img_h/resizeRatio]
        n_img_size = [int(round(s)) for s in resize]
        position_list = getBoundary(bg_size,n_img_size,shift)
        resizeDic[resizeRatio] = position_list

    return resizeDic

def main():
    direct = sys.argv[1]
    
    f = h5py.File("testDset.hdf5")
    
    wb_hight,wb_width = 200,200
    bg_size = [wb_width,wb_hight]
    o_image_size = [400,400]

    resize_lower = 3
    resize_upper = 4
    resize_scale = 0.2

    shift = 0
    degree_step = 5

    #level 2
    sortList = getSortList(direct)
    
    #level 3
    imgList = getImageList(sortList)
    degreeList = getDegreeList(degree_step)
    resizeRange = getResizeRange(resize_lower,resize_upper,resize_scale)

    imgListIndexs = range(len(imgList))
    degreeListIndexs = range(len(degreeList))
    resizeRangeIndexs = range(len(resizeRange))
    
    resizeDic = getPositionCor(resizeRange,bg_size,o_image_size,shift)

    print imgListIndexs
    print degreeListIndexs
    print resizeRangeIndexs
    
    dIndexSet = np.ones((len(imgListIndexs),len(degreeListIndexs),len(resizeRangeIndexs)))
    operationIndexList = getOperationIndexList(imgListIndexs,degreeListIndexs,resizeRangeIndexs)

    
    """ dimension = 3 (variance) + 2(image) : no position variance """
    dSet = f.create_dataset("dSet",(len(imgListIndexs),len(degreeListIndexs),len(resizeRangeIndexs),wb_width,wb_hight),chunks = (1,1,1,wb_width,wb_hight),dtype = np.float32,compression = "gzip")
    
    """ dimension = 1 + 2(image) """
   # dSet = f.create_dataset("dSet",(len(operationIndexList),wb_width,wb_hight))
    print len(dIndexSet)
    print len(dIndexSet[0])
    print len(dIndexSet[0][0])
    print " hope I can see this line !"

    print len(operationIndexList)
    print operationIndexList[-1]

    """ variance contorl  """

    counter = 0
    """start generate variance """

    for operationIndex in operationIndexList:
        """ index for variance information"""
        global counter
        global begin_time
        global end_time

        if counter == 0:
            begin_time= time.time()
            start_time = begin_time

        imgIndex,degreeIndex,resizeIndex = operationIndex
        
        """ get information for variance operation """
        img = imgList[imgIndex]
        degree = degreeList[degreeIndex]
        resizeRatio = resizeRange[resizeIndex]
        
        """ prepare data for variance """
        image = array2Img(img)
        imageSize = getImgSize(image)
        width,height = imageSize
        resize = [width/resizeRatio,height/resizeRatio]
        
        positionlist = resizeDic[resizeRatio]
        w,h = positionlist
        
        """ variance operation start """
        rimg = getRotateImg(image,degree)
        rsimg = getResizeImg(rimg,resize)
        timg = getTransImg(rsimg)

        #position_list = getBoundary(bg_size,timg.size)
        #w_co,h_co = position_list
        
        #print " the size of image is: " + str(timg.size)
        #print " the size of position variance is: " + str(len(w_co)*len(h_co))
        
        #positionCounter = 0
        #for w in w_co:
        #    for h in h_co:
                
        #        wb_img = getWhiteImg(wb_hight,wb_width)
        #        p_img = getPositionImg(wb_img,timg,w,h)

        #        d_img = img2Array(p_img)
                
        #        dSet[positionCounter] = d_img
        #        positionCounter = positionCounter +1
        #        if positionCounter == 10:
        #            p_img.show()
        #timg.show()
        #            f.flush()
        #       break
        
        wb_img = getWhiteImg(wb_hight,wb_width)
        p_img = getPositionImg(wb_img,timg,w,h)
        
        d_img = img2Array(p_img)
        
        
        """ dimention 1 + image(2) """
        #dSet[counter]=d_img
        dSet[imgIndex,degreeIndex,resizeIndex] = d_img
        

        counter += 1
        if counter%100== 0:
            end_time = time.time()
            seconds = end_time-start_time
            start_time = time.time()
            print str(counter) + " :variance chian finished in " + str(seconds) + "seconds"
            
            wait = (len(operationIndexList)-counter)*seconds/100
            wait_m = int(round(wait/60))
            wait_s = wait%60

            print " Need about: <<  " + str(wait_m) + "  >> minutes. << "+ str(wait_s) + " >> seconds to finish"
            

        #print "this for loop run for: "+ str(end_time-start_time)+" seconds"
        #print "imgIndex: " + str(imgIndex)
        #print "degreeIndex: " + str(degreeIndex)
        #print "resizeIndex: " + str(resizeIndex)
        
        
        if counter == 99: 
            image.show()
            timg.show()
            p_img.show()

    print " The total cost of time is: " + str((end_time-begin_time)/60) + " minutes."

if __name__ == "__main__":
    main()
