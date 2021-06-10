#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re 
from color import *

def drop_sob(commit_log):
    for i in range(0, len(commit_log)):
        if (commit_log[i] == ''):
            line = i;
        obj = re.match("Signed\-off\-by: .*", commit_log[i])
        if(obj):
            break
    line = len(commit_log) - line
    while (line > 0):
        print(commit_log.pop())
        line = line - 1;


class patch_header:
    path        = ''
    commit_id   = ''    # bit 0
    author      = ''    # bit 1
    email       = ''    # bit 1
    date        = ''    # bit 3
    subject     = ''    # bit 4
    temp_str    = []
    commit_log  = []
    hunts       = []
    re_dic = {
            "commit_id" :"^From\s(\w{40}).*",
            "author"    :"^From:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "date"      :"",
            "subject"   :"^Subject:\s\[(.*)\]\s(.*)",
            "error"     :"",
            }

    def __init__(self, path):
        self.temp_str.clear()
        self.commit_log   =[]
        self.hunts        =[]
        self.path         = path

    def __str__(self):
        print_c ("sc_b_blue", "commit_id: \t[{}]".format(self.commit_id))
        print_c ("sc_b_blue", "author: \t[{}]".format(self.author))
        print_c ("sc_b_blue", "email: \t\t[{}]".format(self.email))
        print_c ("sc_b_blue", "subject: \t[{}]".format(self.subject))
        print_c ("sc_b_blue", "commit_log: \t{}".format(self.commit_log))
        print_c ("sc_b_blue", "hunts: \t\t{}".format(self.hunts))
        return ""
        #return ("sc_b_blue", "commit_id: \t[{}]\nauthor: \t[{}]\nemail: \t\t[{}]\nsubject: \t[{}]\ncommit_log:\t{}\nhunts:\t{}\n".format( self.commit_id, self.author, self.email, self.subject, self.commit_log, self.hunts))

    def re_match(self, restr, s, group):
        #print("{}:{}".format(restr, s))
        searchObj = re.match(restr, s, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            result = searchObj.group(group)
            return result
        else:
            print ("Can't find anything with pattern({})".format(restr))

    def re_search(self, restr, s, group):
        #print("{}:{}".format(restr, s))
        searchObj = re.search(restr, s, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            result = searchObj.group(group)
            print(result)
            return result
        else:
            print ("Can't find anything with pattern({})".format(restr))

    def get_commit_id(self, s):
        restr = self.re_dic.get("commit_id")
        self.commit_id = self.re_search(restr, s, 1)

    def get_author(self, s):
        restr = self.re_dic.get("author")
        self.author = self.re_search(restr, s, 1)

    def get_email(self, s):
        restr = self.re_dic.get("author")
        self.email = self.re_search(restr, s, 2)

    def get_subject(self, s):
        restr = self.re_dic.get("subject")
        self.subject = self.re_search(restr, s, 2)

    def get_commit_log(self, s):
        for l in s:
            #if (len(l.strip()) == 0):
            #    continue
            if (l.strip() == "---"):
                break;
            self.commit_log.append(l.strip())
        line = 0;
        print(len(self.commit_log))
        print(self.commit_log)
        drop_sob(self.commit_log)

    def fill_data(self, commit_str):
        #print(commit_str)
        self.temp_str = commit_str.split('\n') 
        #print(self.temp_str)
        self.get_commit_id(self.temp_str[0])
        self.get_author(self.temp_str[1])
        self.get_email(self.temp_str[1])
        self.get_subject(self.temp_str[3] + self.temp_str[4])
        #print(self.temp_str[5:])
        self.get_commit_log(self.temp_str[5:])

""" --- End of class patch_header --- """

class commit_header:
    commit_id   = ''    # bit 0
    author      = ''    # bit 1
    email       = ''    # bit 1
    date        = ''    # bit 3
    subject     = ''    # bit 4
    temp_str    = []
    commit_log  = []
    hunts       = []
    re_dic = {
            "commit_id" :"^commit\s(\w{40})",
            "author"    :"^Author:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "date"      :"",
            "subject"   :"^Subject:\s\[(.*)\]\s(.*)",
            "error"     :"",
            }

    def __init__(self):
        self.temp_str.clear()
        self.commit_log   =[]
        self.hunts        =[]

    def __str__(self):
        print_c ("sc_b_yellow", "commit_id: \t[{}]".format(self.commit_id))
        print_c ("sc_b_yellow", "author: \t[{}]".format(self.author))
        print_c ("sc_b_yellow", "email: \t\t[{}]".format(self.email))
        print_c ("sc_b_yellow", "subject: \t[{}]".format(self.subject))
        print_c ("sc_b_yellow", "commit_log: \t{}".format(self.commit_log))
        print_c ("sc_b_yellow", "hunts: \t\t{}".format(self.hunts))
        return ""
        #return ("commit_id: \t[{}]\nauthor: \t[{}]\nemail: \t\t[{}]\nsubject: \t[{}]\ncommit_log:\t{}\nhunts:\t{}\n".format( self.commit_id, self.author, self.email, self.subject, self.commit_log, self.hunts))

    def re_match(self, restr, s, group):
        #print("{}:{}".format(restr, s))
        searchObj = re.match(restr, s, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            result = searchObj.group(group)
            return result
        else:
            print ("Can't find anything with pattern({})".format(restr))

    def re_search(self, restr, s, group):
        searchObj = re.search(restr, s, re.M|re.I)
        if searchObj:
            result = searchObj.group(group)
            print(result)
            return result
        else:
            print ("Can't find anything with pattern({})".format(restr))

    def get_commit_id(self, s):
        restr = self.re_dic.get("commit_id")
        self.commit_id = self.re_search(restr, s, 1)

    def get_author(self, s):
        restr = self.re_dic.get("author")
        self.author = self.re_search(restr, s, 1)

    def get_email(self, s):
        restr = self.re_dic.get("author")
        self.email = self.re_search(restr, s, 2)

    def get_subject(self, s):
        restr = self.re_dic.get("subject")
        self.subject = self.re_search(restr, s, 2)

    def fill_data(self, commit_str):
        #print(commit_str)
        flag = 0
        i = 0
        self.temp_str = commit_str.split('\n') 
        for l in self.temp_str:
            if (i == 0):
                self.get_commit_id(l)
                i = i + 1
                continue;
            if (i == 1):
                self.get_author(l)
                self.get_email(l)
                i = i + 1
                continue
            if (i == 2):
                self.date = l.strip()
                i = i + 1
                continue
            if (i == 4):
                self.subject = l.strip()
                flag |= 0x8;
                i = i + 1
                continue
            if (0 == (flag & 0x8) and len(l.strip()) == 0):
                i = i + 1
                continue
            if (i == 3 or i == 5):
                i += 1;
                continue;

            self.commit_log.append(l.strip())
            i = i + 1
        drop_sob(self.commit_log)


""" --- End of class commit_header --- """

class hunt:
    position = ''

""" --- End of class hunt --- """


