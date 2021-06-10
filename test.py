#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys, getopt
from filter import *
from color import *
from find import get_commit_headers, patch_to_patch_header

def re_search(restr, s, group):
    searchObj = re.search(restr, s, re.M|re.I)
    if searchObj:
        result = searchObj.group(group)
        print(result)
        return result
    else:
        return "" #print ("Can't find anything with pattern({})".format(restr))

def collect_files(patches):
    filelist=[]
    newfile=[]
    for patch in patches:
        file = patch.strip()
        if (True != os.path.isfile(file)):
            print_fatal("[{}] is not a file".format(file))
            sys.exit(1)
        print_info(file)

        f = open(file, mode='r')
        restr = 'diff \-\-git a\/(.*) b\/(.*)'
        for line in f:
            #print(line)
            afile = re_search(restr, line, 1)
            bfile = re_search(restr, line, 2)
            if afile and bfile:
                print("afile = {} bfile = {}".format(afile, bfile))
                if afile == bfile:
                    if (True != os.path.isfile(afile)):
                        print_fatal("[{}] is not exist".format(afile))
                        newfile.append(afile)
                        continue;
                    filelist.append(afile)
        f.close()

    print(filelist)
    print(len(filelist))
    list2 = list(set(filelist))
    for l in list2:
        print(l)
    print(len(list2))
    print("\n")

    print(newfile)

def main(argv):
    #test_color()
    inputfile = '.'
    outputfile = ''    ## reverse
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
        # -- we should add a function to parse "changed.tmp"
 
    cmd = "ls " + inputfile + "/*.patch 2>/dev/null | sort"
    patches = os.popen(cmd) # 列出文件夹下所有的目录与文件

    collect_files(patches)

if __name__ == "__main__":
   main(sys.argv[1:])
