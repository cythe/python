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

def print_c(c, s):
    head=switch.get(c, '\033[m')
    tail='\033[m'
    print(head+s+tail)
