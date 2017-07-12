# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 21:25:13 2014

@author: 27182_000
"""

# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

ans = 1

for n in range(999,1,-1):
    for m in range(999,1,-1):
        num = n*m
        if str(num) == str(num)[::-1] and num > ans:
            ans = num
print ans