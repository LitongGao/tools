#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import time

template = "PathFile, filename={filelist} "
path = sys.argv[1]

timestamp = int(time.time()) * 1000000000
filelist = []
files = ''
for filename in os.listdir(path):
    filelist.append(filename)
    files += filename + "_"
path_file_num = len(filelist)
# filelist = ''.join(str(filelist).split())

# data = template.format(num=path_file_num, filelist=filelist, timestamp=timestamp)
data = 'PathFile,file_status=new filenames="' + files[:-1] + '",file_num=' + str(path_file_num) + " "
print(data + str(timestamp))
sys.exit(0)
