# -*- coding: utf-8 -*-
"""
Created on Mon Jul 07 23:33:59 2014

@author: Eric Cotner

Monty Carlo algorithm for computing pi. Randomly generates (x,y) coordinates in
the region [0,1]x[0,1], then checks to see if they are in the positive quadrant
of the unit circle. If so, a counter is iterated. After many steps, the ratio
of the counter to the total number of iterations should approach the value of
pi/4 (being that we are only computing the area of a single quadrant).
"""

# initialize variables
x = 0
y = 0
pi_count = 0
total_count = 0
pi_approx = 0

# the algorithm
while(total_count < 10**8):
    x = random()                            # generate random (x,y) coordinate
    y = random()
    if x**2 + y**2 <= 1:                    # check if inside unit circle
        pi_count = pi_count + 1             # iterate pi_counter if so
    total_count = total_count + 1           # iterate total steps
pi_approx = (4.0*pi_count) / total_count    # compute pi from ratio
print 'Pi is approximately', pi_approx      # print that shit!