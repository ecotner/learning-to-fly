# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 14:28:13 2014

@author: 27182_000
"""

# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

num = 21
while True:
    j = 0
    for i in range(2,20+1):
        if num % i == 0:
            j += 1
        else:
            break
    if j == 20-1:
        print num
        break
    num += 1       