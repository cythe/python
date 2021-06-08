#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
from ds import *

file = open('tmp', mode='r')

restr= 'commit \w{40}\n'
buffer=file.read()

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
        commit_list.append(commit_header(string))
        print(commit_list)
    
print('start={}, end={}\n'.format(last_slice, len(buffer)))
#print('[' + buffer[last_slice:] + ']')
print('++++++++++++++')
commit_list.append(commit_header(buffer[last_slice:]))

for x in commit_list:
    print(x)

#file.seek(0)
#
#for line in file:
#    print(line)

file.close()


