# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 15:39:12 2014

@author: 27182_000
"""

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
# What is the 10,001st prime number?

primes = [2]
num = 2

while len(primes) < 10001:
    pcount = 0
    for p in primes:
        if num % p == 0:
            break
        else:
            pcount += 1
    if pcount == len(primes):
        primes.append(num)
    num += 1

print primes[len(primes)-1]