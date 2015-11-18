#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:50:31 2015

@author: bingqing.xie
"""

import sys
import os
import time
import re
import jieba
from optparse import OptionParser
from seg_config import *

jieba.load_userdict(r'E:\SolutionModel\WordFreq\dependence\user_dict.txt')

def term_seg(text,str_splitTag):
    seg_text =""
    line = jieba.cut(text,cut_all=False,HMM=True)
    seg_text = str_splitTag.join(line)
    return seg_text
       
def file_seg(in_filename,indexes,out_filename,str_splitTag):
    f = open(in_filename,'r')
    fw = open(out_filename,'w')
    for line in f:
        text = line.strip()
        fw.write(term_seg(text,str_splitTag).encode("utf-8"))               
        fw.write("\n")
    fw.close()
    f.close()


# file_seg(in_filename=in_filename,
# indexes=[0],
# out_filename=out_filename,
# str_splitTag=str_splitTag)

file_seg(in_filename,
indexes,
out_filename,
str_splitTag)