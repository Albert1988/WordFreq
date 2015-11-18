#!/usr/bin/python
#_*_ coding: utf-8 _*_
# author:bingqing.xie
# Filename: WordFreq.py

import sys
import os
from collections import *
from wordfreq_config import *

def wordfreq(corpus_path, start_index, stop_words_path, freq_path):
    corpus = open(corpus_path, 'r')
    vocab_list = []
    for line in corpus.readlines():
        term = line.strip().split(' ')[start_index: ]
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
        freqfile.write(str(item[0]) + '\t' + str(item[1]) + '\n')
    corpus.close()
    freqfile.close()

wordfreq(corpus_path, start_index, stop_words_path,freq_path)
