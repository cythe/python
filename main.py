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
    gitrange = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile=","range="])
    except getopt.GetoptError:
        print_fatal("main.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_info('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--range"):
            gitrange = arg
    print_info("Patches directory: ", inputfile)
    print_info("Log file location: ", outputfile)

    if(gitrange):
        cmd = "git whatchanged " + gitrange + " 1>changed.tmp 2>/dev/null"
        print(cmd)
        os.popen(cmd)
 
    cmd = "ls " + inputfile + "/*.patch 2>/dev/null | sort"
    patches = os.popen(cmd) # 列出文件夹下所有的目录与文件
    for patch in patches:
        file = patch.strip()
        if (True != os.path.isfile(file)):
            print_fatal("it's not a file [{}]".format(file))
            sys.exit(1)
        print_debug(file)
        ph = patch_to_patch_header(file)
        print(ph)
        chs = get_commit_headers(ph.subject)
        print("There are {} commit_headers.".format(len(chs)))
        if (len(chs) == 0):
            continue;
        for i in range(0, len(chs)):
            print(chs[i])
            
        ret = filter_whole(ph, chs)

        #ret = filter_hunt(ph, chs)
        #if (ret != -1):
        #    print_c (""find )



if __name__ == "__main__":
   main(sys.argv[1:])
