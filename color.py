#!/usr/bin/python3
# -*- coding: UTF-8 -*-

switch = {  "sc_red"     :'\033[0;31m',
            "sc_b_red"   :'\033[1;31m',
            "sc_green"   :'\033[0;32m',
            "sc_b_green" :'\033[1;32m',
            "sc_yellow"  :'\033[0;33m',
            "sc_b_yellow":'\033[1;33m',
            "sc_blue"    :'\033[0;34m',
            "sc_b_blue"  :'\033[1;34m',
            "sc_purple"  :'\033[0;35m',
            "sc_b_purple":'\033[1;35m',
            "sc_cyan"    :'\033[0;36m',
            "sc_b_cyan"  :'\033[1;36m',
            "sc_white"   :'\033[0;37m',
            "sc_b_white" :'\033[1;37m',
          }


def print_c(c, *s):
    string = ''
    head=switch.get(c, '\033[m')
    tail='\033[m'
    string += head
    for i in range(0, len(s)):
        string += s[i]
    string += tail
    print(string)


def print_cd(*s):
    string = ''
    tail='\033[m'
    for i in range(0, len(s)):
        head = switch.get(s[i])
        if head:
            string += head
            continue;
        else:
            string += s[i]
            continue;
    string += tail
    print(string)


def print_error(*s):
    print_c('sc_red', *s)

def print_fatal(*s):
    print_c('sc_b_red', *s)

def print_debug(*s):
    print_c('sc_white', *s)

def print_info(*s):
    print_c('sc_green', *s)

def test_color():
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

