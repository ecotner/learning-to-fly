# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 22:54:20 2014

@author: 27182_000
"""

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

This version (1.1) tries to create a matrix whose elements are the number of
unique paths that terminate at that position on the grid. Each iteration
advances the paths by one unit until they all converge at the endpoint. Maybe
I should try using Numpy to solve this after I figure out the method.

ACTUALLY... Basically arrived at this algoritm by accident. What it does is
instead of iterating over entire matrices, it iterates over the elements of
the initial matrix with the same instruction set as before, only this is much
efficient. It still doesn't explain why the iterate() function is overwriting
the grid variable with the temp_grid variable without being told to.

It should be noted that this problem can be solved exactly by considering the
set of all permutations of an instruction set consisting of R (move right) and
D (move down), which results in (2n)!/(n!)^2 possibilites. For an nxm box, this
generalizes to (n+m)!/(n!m!).
"""

# WHY DOES THIS WORK??!!

box_dim = 20 + 1

def iterate(grid):
    temp_grid = grid
    for i in range(box_dim):
        for j in range(box_dim):
            gridij = grid[i][j]
            if gridij != 0 and i == box_dim-1 and j != box_dim-1:
                temp_grid[i][j] = 0
                temp_grid[i][j+1] += gridij
            elif gridij != 0 and j == box_dim-1 and i != box_dim-1:
                temp_grid[i][j] = 0
                temp_grid[i+1][j] += gridij
            elif gridij != 0 and (i != box_dim-1 or j != box_dim-1):
                temp_grid[i][j] = 0
                temp_grid[i+1][j] += gridij
                temp_grid[i][j+1] += gridij
    return temp_grid

# initialize the grid
path_grid = [[0 for i in range(box_dim)] for j in range(box_dim)]
path_grid[0][0] = 1

path_grid = iterate(path_grid)


print path_grid[box_dim-1][box_dim-1]