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

file = open

ret = get_commit_log("test mama ya ")
buffer=''
for a in ret:
    buffer += a
print (buffer)
commit_logs = re.finditer(restr, buffer, re.M|re.I|re.S)
#commit_logs = re.split( restr, buffer, re.M|re.S)

commit_list = []
last_slice = 0
print (commit_logs)

for match in commit_logs:
    if(match.start()):
        print('start={}, end={}\n'.format(last_slice, match.start()))
        string=buffer[last_slice:match.start()]
        #print('[' + string + ']')
        last_slice = match.start()
        print('--------------')
        #print(string)
        print('==============')
        x = commit_header(string)
        x.fill_data(string)
        commit_list.append(x)
        print(commit_list)
    
print('start={}, end={}\n'.format(last_slice, len(buffer)))
#print('[' + buffer[last_slice:] + ']')
print('++++++++++++++')
commit_list.append(commit_header(buffer[last_slice:]))

for x in commit_list:
    print(x)

