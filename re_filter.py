#!/usr/bin/env python

''' This file is to get the lines from file1 which match specified string,\
and write in another file'''

import sys
import re

f= open("orginal.txt",'r')
result = open("result.txt",'w')

for line in f.readlines():
    if re.search(sys.argv[1], line):
        result.write(line)
f.close()
result.close()