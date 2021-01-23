'''
Author: LawsonAbs
Date: 2021-01-23 20:55:25
LastEditTime: 2021-01-23 21:01:42
FilePath: /tools/wordcount.py
计算词频的一个程序
'''


import sys
import os

# 计算该文件中所有单词的词频
def calc(path):
    pass

# 只支持txt文件
def wordcount(path):
    if os.path.isdir(path): # 如果是文件夹         
        fileName = os.listdir(path) # 获取该文件夹下的所有文件        
        pass
    elif os.path.isfile(path) : # 如果是个文件
        pass

if __name__ == "__main__":
    path = ''
    wordcount()