# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:18:53 2017

@author: 27182_000
"""

"""
What is the sum of the digits of 2^1000?
"""

num = str(2**1000)

total = 0
for c in num:
    total += int(c)
print total