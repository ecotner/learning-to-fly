# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:20:03 2017

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

@author: 27182_000

After looking at the forums, this seems like it might be overkill (and not the most efficient method), but here's
what I did:
1) establish the Path class, the objects of which contain all the information that you would want about a path: sum
of the values along the path (size), the actual path taken, and the beginning and end points.
2) create a method which advances the path in a certain direction, consistently updating all Path object attributes
3) devise a function for searching through N successive levels for the path with the largest sum (findPath).
4) advance the maxPath along the direction indicated by the function mentioned in (3)
5) repeat (4) as necessary until the end of the triangle is reached
*) In the future I might want to update this to return the top M largest paths and evolve them all in parallel; this
will lower the probability of the algorithm getting caught in a local minimum (technically maximum), and only results
in an increase in complexity of M

The order of complexity is going to be O(SIZE*M*2^N), so the major bottleneck is the exponential dependence of the
search algorithm

The accepted algorithm seems to be to start from the bottom, take adjacent pairs of values, and then add them to the
row above, then repeat. This doesn't retain the path information (although I think it could be modified easily to
include it), but it does get the max value.
"""

import numpy as np
import string
import time

t0 = time.time()

#define triangle array
triString = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 '''


# turn string into array by constructing buffer that reads in elements of string, then writes to array when space or
# newline is detected
SIZE = triString.count('\n') + 1
tri = np.zeros((SIZE,SIZE), int)
buff = ''
row, col = 0, 0
for c in triString:
    if c in string.digits:
        buff += c
    elif c == ' ':
        tri[row,col] = int(buff)
        col += 1
        buff = ''
    elif c == '\n':
        tri[row,col] = int(buff)
        col = 0
        row += 1
        buff = ''

# define Path class which contains information on the path route and size
class Path(object):
    '''Path information class; contains info on path through triangle'''
    array = np.copy(tri)
    def __init__(self, rowStart, colStart):
        self.rowStart = rowStart
        self.colStart = colStart
        self.rowFin = rowStart
        self.colFin = colStart
        self.path = ''
        self.size = Path.array[rowStart, colStart]
    #define comparisons between paths by total path size    
    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False
    def __le__(self, other):
        if self.size <= other.size:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.size > other.size:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.size >= other.size:
            return True
        else:
            return False
    def _eq__(self, other):
        if self.size == other.size:
            return True
        else:
            return False
    def _ne__(self, other):
        if self.size != other.size:
            return True
        else:
            return False
    # not totally necessary, but prints a Path object as its path set
    def __str__(self):
        return self.path
    # function for advancing the path either left ('L') or right ('R')
    def advPath(self, direction):
        if direction not in 'LR':
            raise ValueError('Incorrect direction input')
        elif direction == 'L':
            self.rowFin += 1
            #self.colFin += 0
            self.size += Path.array[self.rowFin, self.colFin]
            self.path += 'L'
        elif direction == 'R':
            self.rowFin += 1
            self.colFin += 1
            self.size += Path.array[self.rowFin, self.colFin]
            self.path += 'R'
# function for searching through all available paths by looking at the next 2^nLevels number of possible paths and
# returning the largest path based on maximum path.size
def findPath(rowStart, colStart, nLevels):
    pathList = [Path(rowStart, colStart) for i in range(2**nLevels)]
    def findPathHelper(p):
        if len(p) <= 2:
            p[0].advPath('L')
            p[1].advPath('R')
        else:
            partition = len(p)/2
            for i in range(0,partition):
                p[i].advPath('L')
            for i in range(partition,2*partition):
                p[i].advPath('R')
            findPathHelper(p[:partition])
            findPathHelper(p[partition:])
        return p
    findPathHelper(pathList)
    return max(pathList)

# initialize parameters
maxPath = Path(0,0)
N = 12
# recursively test each potential pathway, advance the position in the most favorable direction, and repeat
for row in range(SIZE - (N-1) - 2):
    localMaxPath = findPath(maxPath.rowFin, maxPath.colFin, N)
    direction = localMaxPath.path[0]
    maxPath.advPath(direction)
if maxPath.rowFin < (SIZE-1):
    localMaxPath = findPath(maxPath.rowFin, maxPath.colFin, N)
    for d in localMaxPath.path:
        maxPath.advPath(d)


# return final answers
print('Max path value: {0}.\nPath directions: {1}.\nFinal path level: {2}.\nTime elapsed: {3}.'.format(maxPath.size, maxPath.path, maxPath.rowFin, time.time()-t0))


        
        
        
        
    








