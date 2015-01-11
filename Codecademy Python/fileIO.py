# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:56:01 2014

@author: 27182_000
"""
xpoints = range(11)
ypoints = [e**i for i in xpoints]

def write_points(x,y):
    with open('text.txt', 'w') as f:
        for i in x:
            f.write(str(x[i]) + ',' + str(y[i]) + '\n')

def read_points(a):
    with open('text.txt', 'r') as f:
        for i,line in enumerate(f):
            if i == a:
                return line

write_points(xpoints,ypoints)
print read_points(10)