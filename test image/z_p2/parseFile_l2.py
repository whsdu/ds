#!/usr/bin/env python
import sys
import glob

def getSortList(direct):
    direct = direct + "*.jpg"
    fileNume = len(glob.glob(direct))
    
    # scalar of level 3 variance 
    scaleV3 = fileNume

    sortList= range(fileNume)
    
    for infile in glob.glob(direct):
        string = infile.split("_")
        sortList[int(string[3])] = infile

    return sortList


def main():
    direct = sys.argv[1]
    print direct
    testGetSortList(direct)

def testGetSortList(direct):
    datalist = getSortList(direct)
    
    for f in datalist:
        print f
    print "totle number of files continedis: " + str(len(datalist))

if __name__ == "__main__":
    main()

