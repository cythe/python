#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os
#from color import *
from ds import *

c_adj=['const', 'unsigned', 'signed']
c_type=['int', 'void', 'short', 'long', 'float', 'double']
c_adt=['struct', 'union']

def filter_whole(ph, chs):
    print_c ("sc_red", "filter whole patch")
