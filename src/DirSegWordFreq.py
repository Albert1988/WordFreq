# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:24:49 2015

@author: bingqing.xie
"""

import os
import jieba
from collections import Counter
from DirSegWordFreq_config import *

jieba.load_userdict(user_dict_path)

def term_seg(text,str_splitTag):
    seg_text =""
    line = jieba.cut(text,cut_all=False,HMM=True)
    seg_text = str_splitTag.join(line)
    return seg_text
       
def file_seg(in_filename,out_filename,str_splitTag):   
    f = open(in_filename,'r')
    fw = open(out_filename,'w')
    for line in f:
        text = line.strip()
        fw.write(term_seg(text,str_splitTag).encode("utf-8"))               
        fw.write("\n")
    fw.close()
    f.close()

def word_freq(corpus_path, stop_words_path, freq_path):
    corpus = open(corpus_path, 'r')
    vocab_list = []
    for line in corpus.readlines():
        term = line.strip().split(' ')
        vocab_list += term
    freqfile = open(freq_path,'w')
    c = Counter(vocab_list)
    cc = sorted(c.items(), key=lambda d:d[1], reverse=True)
    stop_words = map(lambda x: x.strip(), open(stop_words_path,'r').readlines())
    stop_words_dic = dict()
    for i, stopword in enumerate(stop_words):
        stop_words_dic[stopword] = i
    for item in cc:
        if stop_words_dic.has_key(item[0]) is True:
            continue
        if len(item[0]) < 4:
            continue
        freqfile.write(str(item[0]) + '\t' + str(item[1]) + '\n')
    corpus.close()
    freqfile.close()

def dir_freq(dir, fileinfo_path, str_splitTag, stop_words_path):
    fileinfo = open(fileinfo_path,'w')
    for root, dirnames, filenames in os.walk(dir,topdown=True):
        for name in filenames:
            fileinfo.write(os.path.join(root,name) + '\n')
            fname = os.path.join(root, name)
            fwname = os.path.join(fname+'.seg')
            fqname = os.path.join(fname + '.freq')
            file_seg(fname, fwname, str_splitTag)
            word_freq(fwname, stop_words_path, fqname)
    fileinfo.close()
    
dir_freq(dir,
         fileinfo_path,
         str_splitTag,
         stop_words_path)
