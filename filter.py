#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os
from color import *
from ds import *

c_adj=['const', 'unsigned', 'signed']
c_type=['int', 'void', 'short', 'long', 'float', 'double']
c_adt=['struct', 'union']

def filter_hunts(ph, chs):
    print_error ("Todo : filter hunts")


def filter_whole(ph, chs):
    print_info ("sc_red", "filter whole patch")
    for ch in chs:
        for i in range(0, len(ph.commit_log)):
            if (ph.commit_log[i] == ch.commit_log[i]):
                print_info ("matched.\n")
            else:
                print_error ("broken match at {}".format(i))
                break
        print_cd ("sc_green", "patch", "sc_b_blue", " [{}] ".format(ph.path),
                  "sc_green", "is similar with follow commit:\n")
        print(ch)

        # -- do_some_thing with this patch --
        cmd = "mv " + ph.path + " maybedup/"
        os.popen(cmd)

        
        filter_hunts(ph, chs)
