#!/usr/bin/python3

import os
from color import print_c

def exit_process():
    print_c("sc_b_green", "Bye Bye!")
    exit()

def get_commit_log(subject):
    cmd = 'git log --no-merges --grep="' + subject + '"' + ' 1>commit_log.tmp' + ' 2>/dev/null'
    print(cmd)
    #ret = os.system(cmd)
    #if (ret != 0):
    #    print_c("sc_b_red", "[ERROR]: Your git repo maybe has some trouble. Please check!")
    #    exit_process()
    cmd = 'git log --no-merges --grep="' + subject + '"' + ' 2>/dev/null'
    ret = os.popen(cmd)
    for a in ret:
        print(a)

ret = os.system("git status > /dev/null 2>&1")
if (ret != 0):
    print_c("sc_b_red", "[FATAL]: It's not a git directory.")
    exit_process()

get_commit_log("test mama ya ")
