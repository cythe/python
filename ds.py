#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re 

class common_header:
    commit_id   = ''    # bit 0
    author      = ''    # bit 1
    email       = ''    # bit 1
    date        = ''    # bit 3
    subject     = ''    # bit 2
    commit_log  = []
    hunts       = []
    temp_str    = []

    def __init__(self, commit_str):
        self.temp_str     =[]
        self.commit_log   =[]
        self.hunts        =[]

    def re_match(self, restr, s, group):
        print("{}:{}".format(restr, s))
        searchObj = re.match(restr, s, re.M|re.I)
        if searchObj:
            print ("searchObj.group() : ", searchObj.group())
            result = searchObj.group(group)
            return result
        else:
            print ("Can't find anything with pattern({})".format(restr))

    def re_search(self, restr, s, group):
        print("{}:{}".format(restr, s))
        searchObj = re.search(restr, s, re.M|re.I)
        if searchObj:
            print ("searchObj.group() : ", searchObj.group())
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
        restr = self.re_dic.get("email")
        self.email = self.re_search(restr, s, 2)

    def get_subject(self, s):
        restr = self.re_dic.get("subject")
        self.subject = self.re_search(restr, s, 2)

    def __str__(self):
        return ("commit_id: \t[{}]\nauthor: \t[{}]\nemail: \t\t[{}]\nsubject: \t[{}]\ncommit: \t{}\nhunts: \t{}".format( self.commit_id, self.author, self.email, self.subject, self.commit_log, self.hunts))

class patch_header(common_header):
    re_dic = {
            "commit_id" :"From\s(\w{40}).*",
            "author"    :"From:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "email"     :"From:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "date"      :"",
            "subject"   :"Subject:\s\[(.*)\]\s(.*)",
            "error"     :"",
            }

    def get_commit_log(self, s):
        print('This is the re')
        #searchObj = re.search( r'.*\ndiff\s--git\s([^\s]*)\s([^\s]*)', s, re.M|re.I)
        commit_logs = re.split( restr, buffer, re.M|re.S)
        searchtest= re.split( r'(^---$)', self.__temp_str, re.M|re.I)
        print (searchtest)

    def fill_data(self, commit_str):
        print(commit_str)
        self.__temp_str = commit_str.split('\n') 
        print(self.__temp_str)
        self.get_commit_id(self.__temp_str[0])
        self.get_author(self.__temp_str[1])
        self.get_email(self.__temp_str[1])
        self.get_subject(self.__temp_str[3] + self.__temp_str[4])
        #get_commit_log(self

""" --- End of class patch_header --- """

class commit_header(common_header):
    re_dic = {
            "commit_id" :"commit\s(\w{40})",
            "author"    :"Author:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "email"     :"Author:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>",
            "date"      :"",
            "subject"   :"Subject:\s\[(.*)\]\s(.*)",
            "error"     :"",
            }

    def fill_data(self, commit_str):
        print(commit_str)
        flag = 0
        i = 0
        print(commit_str)
        self.__temp_str = commit_str.split('\n') 
        for l in self.__temp_str:
            if (len(l.strip()) == 0):
                i = i + 1
                continue
            if (i == 0):
                self.__commit_id = self.get_commit_id(l)
                i = i + 1
                continue;
            if (i == 1):
                self.__author,self.__email = self.get_author(l)
                i = i + 1
                continue
            if (i == 2):
                self.__date = l.strip()
                i = i + 1
                continue
            if (0 == (flag & 0x8)):
                self.__subject = l.strip()
                flag |= 0x8;
                i = i + 1
                continue
            self.__commit_log.append(l.strip())
            i = i + 1


""" --- End of class commit_header --- """

class hunt:
    position = ''

""" --- End of class hunt --- """


