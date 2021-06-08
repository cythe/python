#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os
from color import print_c
from ds import *
from find import *

def exit_process():
    print_c("sc_b_green", "Bye Bye!")
    exit()

def get_commit_log(subject):
    #cmd = 'git log --no-merges --grep="' + subject + '"' + ' 1>commit_log.tmp' + ' 2>/dev/null'
    #print(cmd)
    #ret = os.system(cmd)
    #if (ret != 0):
    #    print_c("sc_b_red", "[ERROR]: Your git repo maybe has some trouble. Please check!")
    #    exit_process()
    cmd = 'git log --no-merges --grep="' + subject.strip() + '"' + ' 2>/dev/null'
    ret = os.popen(cmd)
    return ret


ret = os.system("git status > /dev/null 2>&1")
if (ret != 0):
    print_c("sc_b_red", "[FATAL]: It's not a git directory.")
    exit_process()

restr= 'commit \w{40}\n'

ret = get_commit_log("test mama ya ")
buffer=''
for a in ret:
    buffer += a
print ("buffer = {}".format(buffer))
commit_logs = re.finditer(restr, buffer, re.M|re.I|re.S)
#commit_logs = re.split( restr, buffer, re.M|re.S)

commit_list = []
last_slice = 0

for match in commit_logs:
    if(match.start()):
        print('start={}, end={}\n'.format(last_slice, match.start()))
        string=buffer[last_slice:match.start()]
        print('[' + string + ']')
        last_slice = match.start()
        print('--------------')
        print(string)
        print('==============')
        x = commit_header(string)
        x.fill_data(string)
        print(x)
        commit_list.append(x)
    

print('start={}, end={}'.format(last_slice, len(buffer)))
print('++++++++++++++++++++')
string = buffer[last_slice:]
x = commit_header(string)
x.fill_data(string)
print(x)
commit_list.append(x)

print(len(commit_list))
