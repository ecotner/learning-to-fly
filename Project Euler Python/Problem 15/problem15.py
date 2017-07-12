# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 14:21:34 2014

@author: 27182_000
"""

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

This version (1.0) tried to split each path into its own element of a vector,
which eventually failed because the length of the vector was a little bit less
than 2^(2n) where n is the dimensions of the box. For n=20, the length of the
vector was about 10^12 elements long. VERY memory intensive. Whoops.

It should be noted that this problem can be solved exactly by considering the
set of all permutations of an instruction set consisting of R (move right) and
D(move down), which results in (2n)!/(n!)^2 possibilites. For an nxm box, this
generalizes to (n+m)!/(n!m!).
"""

box_dim = 5
count = 0

def iterate():
    for n in range(len(x)):
        if x[n] == box_dim:
            y[n] += 1
        elif y[n] == box_dim:
            x[n] += 1
        else:
            x.append(x[n])
            y.append(y[n]+1)
            x[n] += 1

x = [0]
y = [0]

for i in range(box_dim*2):
    iterate()
    
for i in range(len(x)):
    if x[i] == box_dim and y[i] == box_dim:
        count += 1

print count