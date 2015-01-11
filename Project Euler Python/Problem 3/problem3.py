# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 08:20:32 2014

@author: 27182_000
"""

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

factors = []
num = 600851475143
i = 1

for i in range(2,int(sqrt(num))):
    while num % i == 0:
        factors.append(i)
        ans = i
        num = num / i
print factors