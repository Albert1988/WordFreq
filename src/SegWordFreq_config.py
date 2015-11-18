# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:50:31 2015

@author: bingqing.xie
"""

file = "UGC"

#自定义词典路径，词典格式：第一项 词  第二项 权重 第三项 词性 各个项之间以空格隔开
user_dict_path = r'E:\SolutionTemp\WordFreq\dependence\user_dict.txt'

#自定义停用词或去除词路径，一个词一行，例如：http
stop_words_path = r'E:\SolutionTemp\WordFreq\dependence\stopwords.txt'

#要分词的文本路径
#in_filename=r"E:\SolutionTemp\WordFreq\data\UGC.txt"
in_filename = "E:/SolutionTemp/WordFreq/data/" + file + ".txt"

#文本分词后的保存路径
#out_filename=r"E:\SolutionTemp\WordFreq\data\UGC_seg.txt"
out_filename = "E:/SolutionTemp/WordFreq/data/" + file + "_seg.txt"
corpus_path = out_filename

#词与词之间的间隔符号，默认为空格
str_splitTag=" "

#关键词和词频文档保存路径
#freq_path = r'E:\SolutionTemp\WordFreq\result\UGC_freq.txt'
freq_path = "E:/SolutionTemp/WordFreq/result/" + file + "_freq.txt"



