#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

#read one line drop one line
def read_and_destroy(f):
    
    per = 1
    
    data = open(f,'r+')
    lines = data.readlines()
    
    for li in lines[:per]:
        do_something(li)
    
    if line[per:]:    
        data.seek(0)
        data.writelines(lines[per:])
        data.truncate()
    data.close()

def do_something(line):
    pass
    
if __name__ == "__main__":
    read_and_destroy('test.txt')












