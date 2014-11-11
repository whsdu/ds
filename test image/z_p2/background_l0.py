#!/usr/bin/env python
import numpy as np

def getWhiteBackground(hight,width):
    wb = np.ones((width,hight))
    wb = wb*255

    return wb

def getNoiseBackbround(hight,width):
    rb = np.random.uniform(low = 0,high = 255,size=(width,hight))
    return rb

def main():
    wb = getWhiteBackground(500,500)
    print len(wb)
    print wb

    rb = getNoiseBackbround(500,500)
    print len(rb)
    print rb
if __name__ =="__main__":
    main()
