# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:11:01 2014

@author: 27182_000
"""

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys

s = 1000

for a in range(1,s+1):
    for b in range(1,s+1):
        for c in range(1,s+1):
            if a + b + c == s:
                if a**2 + b**2 == c**2:
                    print a*b*c
                    sys.exit()
                