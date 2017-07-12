# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:22:53 2014

@author: 27182_000
"""

# Find the sum of all the primes below two million.

maxx = 2000000
primes = range(2, maxx+1)

for n in range(2, maxx+1):
    if primes[n-2] != 0:
        for m in range(2,maxx/n+1):
            primes[m*n-2] = 0

ans=0
for p in primes:
    ans += p
print ans