# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 15:34:46 2014

@author: 27182_000
"""

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sum_of_squares = 0
square_of_sum = 0
num = 0

for i in range(1,101):
    sum_of_squares += i**2
    
for i in range(1,101):
    num += i
square_of_sum = num**2

print sum_of_squares - square_of_sum