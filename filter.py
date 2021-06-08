#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os
from color import *
from ds import *

c_adj=['const', 'unsigned', 'signed']
c_type=['int', 'void', 'short', 'long', 'float', 'double']
c_adt=['struct', 'union']

path = 'patches/test.patch'
def patch_to_patch_header(path):
    file = open(path, mode='r', newline='\n')
    buffer = file.read()
    file.close()
    return buffer

buffer = patch_to_patch_header(path)
print(buffer)

patch_h = patch_header(buffer);
patch_h.fill_data(buffer)
#val = os.system('filter.sh')
print(patch_h)

print_c("sc_red"     ,"red"     )
print_c("sc_b_red"   ,"b_red"   ) 
print_c("sc_green"   ,"green"   ) 
print_c("sc_b_green" ,"b_green" ) 
print_c("sc_brown"   ,"brown"   ) 
print_c("sc_yellow"  ,"yellow"  ) 
print_c("sc_blue"    ,"blue"    ) 
print_c("sc_b_blue"  ,"b_blue"  ) 
print_c("sc_purple"  ,"purple"  ) 
print_c("sc_b_purple","b_purple") 
print_c("sc_cyan"    ,"cyan"    ) 
print_c("sc_b_cyan"  ,"b_cyan"  )
print_c("sc_white"   ,"white"   ) 
print_c("sc_b_white" ,"b_white" ) 

