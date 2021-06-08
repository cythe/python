#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re 

class patch_header:
    __commit_id = ''
    __author = ''
    __email = ''
    __subject = '' 
    __commit_log = ''
    __temp_str = ''

    def __init__(self, commit_str):
        print(commit_str)
        self.__temp_str = commit_str.strip() 
        print(self.__temp_str)
        self.__commit_id = self.get_commit_id();

    def __str__(self):
        return ("__commit_id: \t[{}]\nauthor: \t[{}]\nemail: \t\t[{}]\nsubject: \t[{}]\ncommit: \t[{}]\n".format(self.__commit_id, self.__author, self.__email, self.__subject, self.__commit_log))

    def get_commit_id(self):
        print('This is the for_commit_ID')
        #ret = re.match('From []', line, re.I)
        #(.*?) .*', line, re.M|re.I)
        searchObj = re.search(r'From\s(\w+)', self.__temp_str, re.M|re.I)
        if searchObj:
            print ("searchObj.group() : ", searchObj.group())
            __commit_id = searchObj.group(1)
            print('__commit_id = [' + __commit_id + ']')
            return __commit_id
        else:
            print ("Can't find __commit_id, exit!!")

    def get_author(self):
        print('This is the for_author')
        searchObj = re.search( r'From:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>', self.__temp_str, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            #print ("searchObj.group() : ", searchObj.group(1))
            #print ("searchObj.group() : ", searchObj.group(2))
            __author = searchObj.group(1)
            __email = searchObj.group(2)
            print('__author = [' + __author + ']')
            print('__email = [' + __email + ']')
            return __author,__email
        else:
            print ("Can't find __author , exit!!")

    def get_subject(self):
        print('This is the for_subject')
        searchObj = re.search( r'Subject:\s\[(.*)\]\s(.*)', self.__temp_str, re.M|re.I)
        if searchObj:
            print ("searchObj.group() : ", searchObj.group())
            print ("searchObj.group() : ", searchObj.group(1))
            print ("searchObj.group() : ", searchObj.group(2))
            patch = searchObj.group(1)
            __subject = searchObj.group(2)
            print('patch = [' + patch + ']')
            print('__subject = [' + __subject + ']')
            return __subject
        else:
            print ("Can't find __subject, exit!!")

    def get_commit_log(self):
        print('This is the re')
        #searchObj = re.search( r'.*\ndiff\s--git\s([^\s]*)\s([^\s]*)', s, re.M|re.I)
        commit_logs = re.split( restr, buffer, re.M|re.S)
        searchtest= re.split( r'(^---$)', self.__temp_str, re.M|re.I)
        print (searchtest)

""" --- End of class patch_header --- """

class commit_header:
    __commit_id   = ''    # bit 0
    __author      = ''    # bit 1
    __email       = ''    # bit 1
    __date        = ''    # bit 3
    __subject     = ''    # bit 2
    __commit_log  = []
    __temp_str    = []

    def __init__(self, commit_str):
        self.__temp_str.clear()
        self.__commit_log=[]
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

    def __str__(self):
        return ("__commit_id: \t[{}]\nauthor: \t[{}]\nemail: \t\t[{}]\nsubject: \t[{}]\ncommit: \t{}\n".format(self.__commit_id, self.__author, self.__email, self.__subject, self.__commit_log))

    def get_commit_id(self, s):
        print('This is the for_commit_ID')
        #ret = re.match('From []', line, re.I)
        #(.*?) .*', line, re.M|re.I)
        searchObj = re.search(r'commit\s(\w{40})', s, re.M|re.I)
        if searchObj:
            print ("searchObj.group() : ", searchObj.group())
            __commit_id = searchObj.group(1)
            print('__commit_id = [' + __commit_id + ']')
            return __commit_id
        else:
            print ("Can't find __commit_id, exit!!")

    def get_author(self, s):
        print('This is the for_author')
        searchObj = re.search( r'Author:\s(.*)\s\<(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)\>', s, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            #print ("searchObj.group() : ", searchObj.group(1))
            #print ("searchObj.group() : ", searchObj.group(2))
            __author = searchObj.group(1)
            __email = searchObj.group(2)
            print('__author = [' + __author + ']')
            print('__email = [' + __email + ']')
            return __author,__email
        else:
            print ("Can't find __author , exit!!")

""" --- End of class commit_header --- """

class hunt:
    position = ''

""" --- End of class hunt --- """
