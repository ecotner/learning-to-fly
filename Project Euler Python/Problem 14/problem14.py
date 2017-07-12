# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 14:04:16 2014

@author: 27182_000
"""

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

chain_max = 0

for i in range(2,10**6):
    chain_length = 1
    j = i
    while j != 1:
        chain_length += 1
        j = next_collatz(j)
    if chain_length > chain_max:
        chain_max = chain_length
        chain_max_start = i

print 'the starting number %d has a max chain length %d' % (chain_max_start, chain_max)