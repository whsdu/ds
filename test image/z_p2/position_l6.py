#!/usr/bin/env python
from reSize_l5 import *
from rotate_l4 import *
from dataPrepare_l3 import *
from parseFile_l2 import *
from background_l0 import *

def getPositionImg(wbImg,timg,w,h):
    wbImg.paste(timg,(w,h),timg)
    return wbImg

def img2Array(img):
    imgList = list(img.getdata())
    width, height = img.size
    d_img = [imgList[i * width:(i + 1) * width] for i in xrange(height)]

    return d_img 

def getBoundary(bg_size,img_size,shift):

    bg_width,bg_hight = bg_size
    im_width,im_hight =img_size
    position_list = []

    if shift == 0:
        w = int(round(bg_width/2-im_width/2))
        h = int (round(bg_hight/2-im_hight/2))
        position_list = [w,h]
    
    elif shift > 0 & shift < 100:

        width = bg_width-im_width
        hight = bg_hight-im_hight

        w_step = int(round(im_width/shift))
        h_step = int(round(im_hight/shift))

        w_list = range(0,width,w_step)
        h_list = range(0,hight,h_step)

        position_list = [w_list,h_list]
    else:
        print "incorrect shift ratio, should between [0,100)"
        raise 

    return position_list


def main():
    direct = sys.argv[1]
    #level 2
    sortList = getSortList(direct)
    shift = 0
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
    
#    rsimg.show()
    timg = getTransImg(rsimg)
    
#    timg.show()

    # level  0 , get wb background
    wb_hight = 600
    wb_width = 600
    
    wb = getWhiteBackground(wb_width,wb_hight)
    wbimg = array2Img(wb)

    
    positionList = getBoundary(wbimg.size,timg.size,shift)
    
    # level 6 & 7
        #calculate position range
#    w,h = 150,150
    if shift ==0:
        w,h = positionList
    else:
        w_list,h_list = positionList
        w = w_list[-1]
        h = h_list[-1]
 
    p_img = getPositionImg(wbimg,timg,w,h)
    p_img.show()

    d_img = img2Array(p_img)

    print len(d_img)
    print len(d_img[0])
    print d_img

if __name__ == "__main__":
    main()

