# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 08:14:06 2014

@author: 27182_000
"""

# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

fib1 = 1
fib2 = 2
ans = 0

while fib2 < 4000000:
    if fib2 % 2 == 0:
        ans += fib2
    temp = fib2
    fib2 += fib1
    fib1 = temp
print ans