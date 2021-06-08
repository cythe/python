#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os

from color import *

c_adj=['const', 'unsigned', 'signed']
c_type=['int', 'void', 'short', 'long', 'float', 'double']
c_adt=['struct', 'union']

file = open('test.patch', mode='r', newline='\n')

switch = {1: for_commit_ID,                # 注意此处不要加括号
          2: for_author,
          4: for_subject,
          }

line_n = 1

patch_h = patch_header();
val = os.system('filter.sh')
print ("ret = ", val)
for line in file:
    f = switch.get(line_n, default)            # 执行对应的函数，如果没有就执行默认的函数
    f(patch_h, line)

    line_n += 1;

file.close()
print(patch_h)

print_c("sc_red"     ,"sc_red"     )
print_c("sc_b_red"   ,"sc_b_red"   ) 
print_c("sc_green"   ,"sc_green"   ) 
print_c("sc_b_green" ,"sc_b_green" ) 
print_c("sc_brown"   ,"sc_brown"   ) 
print_c("sc_yellow"  ,"sc_yellow"  ) 
print_c("sc_blue"    ,"sc_blue"    ) 
print_c("sc_b_blue"  ,"sc_b_blue"  ) 
print_c("sc_purple"  ,"sc_purple"  ) 
print_c("sc_b_purple","sc_b_purple") 
print_c("sc_cyan"    ,"sc_cyan"    ) 
print_c("sc_b_cyan"  ,"sc_b_cyan"  )
print_c("sc_white"   ,"sc_white"   ) 
print_c("sc_b_white" ,"sc_b_white" ) 

