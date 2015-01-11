# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 11:14:55 2014

@author: 27182_000
"""

def remove_duplicates(lst):
    if lst == []:
        ans = []
    else:
        dup = [lst[0]]
        ans = [lst[0]]
        for i in lst:
            s = 0
            for j in dup:
                if i == j:
                    s += 1
            if s == 0:
                ans.append(i)
            dup.append(i)
    return ans

print remove_duplicates([])