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

    # level 6 & 7
        #calculate position range
    w,h = 150,150
    p_img = getPositionImg(wbimg,timg,w,h)
    p_img.show()

    d_img = img2Array(p_img)

    print len(d_img)
    print len(d_img[0])
    print d_img
