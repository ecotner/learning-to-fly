# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:22:53 2014

@author: 27182_000
"""

# Find the sum of all the primes below two million.

primes = [2]
n = 2

while n <= 10:
    pcount = 0
    for p in primes:
        if n % p == 0:
            break
        else:
            pcount += 1
    if pcount == len(primes):
        primes.append(n)
    n += 1

ans = sum(primes)
print ans