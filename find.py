#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import os
from color import print_c
from ds import *

def exit_process():
    print_c("sc_b_green", "Bye Bye!")
    exit()


def get_commit_log(subject):
    ret = os.system("git status > /dev/null 2>&1")
    if (ret != 0):
        print_c("sc_b_red", "[FATAL]: It's not a git directory.")
        exit_process()
    cmd = 'git log --no-merges --grep="' + subject.strip() + '"' + ' 2>/dev/null'
    ret = os.popen(cmd)
    return ret


def get_commit_log_from_file(subject):
    return []


# -- Get commit headers by commit subject
def get_commit_headers(subject):
    buffer=''
    last_slice = 0
    commit_list = []
    restr= 'commit \w{40}\n'
    
    ret = get_commit_log(subject)
    for a in ret:
        buffer += a
    print ("buffer = {}".format(buffer))
    if (len(buffer.strip()) == 0):
        return []
    commit_logs = re.finditer(restr, buffer, re.M|re.I|re.S)
    for match in commit_logs:
        if(match.start()):
            #print('start={}, end={}\n'.format(last_slice, match.start()))
            string=buffer[last_slice:match.start()]
            #print('[' + string + ']')
            last_slice = match.start()
            #print("--------------"+string+"--------------")
            x = commit_header()
            x.fill_data(string)
            #print(x)
            commit_list.append(x)
    #print('start={}, end={}'.format(last_slice, len(buffer)))
    #print('++++++++++++++++++++')
    string = buffer[last_slice:]
    x = commit_header()
    x.fill_data(string)
    #print(x)
    commit_list.append(x)
    return commit_list


def patch_to_patch_header(path):
    file = open(path, mode='r', newline='\n')
    buffer = file.read()
    file.close()
    x = patch_header(path);
    x.fill_data(buffer)
    return x
