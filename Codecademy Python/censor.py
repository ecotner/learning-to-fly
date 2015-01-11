# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 21:54:31 2014

@author: 27182_000
"""

def replace(string,position,y):
    ans = ''
    for i,c in enumerate(string):
        if i == position:
            c = y
        ans = ans + c
    return ans

def censor(text,word):
    text1 = text
    for i in range(len(text1)):
        if text1[i:i+len(word)] == word:
            print '!'
            for j in range(len(word)):
                text1 = replace(text1,i+j,'*')
    return text1

print censor('hey, ho! watch it go! hey, ho! watch it go! hey hey hey!','hey')