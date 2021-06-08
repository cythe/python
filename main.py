#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys, getopt
from ds import *

def main(argv):
    inputfile = '.'
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('输入的文件为：', inputfile)
    print ('输出的文件为：', outputfile)
 
    cmd = "ls " + inputfile + "/*.patch | sort"
    patches = os.popen(cmd) # 列出文件夹下所有的目录与文件
    for patch in patches:
        #path = i #os.path.join(inputfile, i)
        # if os.path.isfile(path):
        # # 你想对文件的操作
        print (patch)
        


if __name__ == "__main__":
   main(sys.argv[1:])
