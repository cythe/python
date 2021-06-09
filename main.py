#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys, getopt
from ds import *
from filter import *
from color import *
from find import get_commit_headers, patch_to_patch_header

def main(argv):
    #test_color()
    inputfile = '.'
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print_c ("sc_b_red", "main.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_c ("sc_b_red", 'test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print_c ("sc_b_green", "Patches directory: ", inputfile)
    print_c ("sc_b_green", "Log file location: ", outputfile)
 
    cmd = "ls " + inputfile + "/*.patch 2>/dev/null | sort"
    patches = os.popen(cmd) # 列出文件夹下所有的目录与文件
    for patch in patches:
        file = patch.strip()
        if (True != os.path.isfile(file)):
            print_c ("sc_b_red", "it's not a file [{}]".format(file))
            sys.exit(1)
        print_c ("sc_b_green", file)
        ph = patch_to_patch_header(file)
        print(ph)
        chs = get_commit_headers(ph.subject)
        for i in range(0, len(chs)):
            print(chs[i])
            
        ret = filter_whole(ph, chs)

        #ret = filter_hunt(ph, chs)
        #if (ret != -1):
        #    print_c (""find )



if __name__ == "__main__":
   main(sys.argv[1:])
