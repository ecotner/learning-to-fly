# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 12:25:28 2014

@author: 27182_000
"""

# What is the value of the first triangle number to have over five hundred divisors?

num_divisors = 0
num_divisors_max = 0
n = [1,1]       # first index defines which triangle num, second defines actual num

def next_triangle_num(previous_num):
    next_num = [previous_num[0] + 1, previous_num[1] + previous_num[0] + 1]
    return next_num

while num_divisors <= 500:
    num_divisors = 0
    n = next_triangle_num(n)
    for m in range(1,int(sqrt(n[1]))+1):
        if n[1] % m == 0:
            num_divisors += 2
    if num_divisors > num_divisors_max:
        num_divisors_max = num_divisors
        max_triangle = n[1]
print n[1]