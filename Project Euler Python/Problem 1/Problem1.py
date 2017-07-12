# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 08:07:13 2014

@author: 27182_000
"""

# Find the sum of all the multiples of 3 or 5 below 1000.

ans = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        ans = ans + i
print 'answer is %d.' % ans