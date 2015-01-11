# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 19:35:37 2014

@author: 27182_000
"""

while True:
    sent = raw_input("input phrase: ")
    ans = sent[0]
    if sent.lower() == 'quit':
        break
    else:
        for i in range(len(sent)):
            if sent[i] == ' ':
                ans = ans + sent[i+1]
        print ans