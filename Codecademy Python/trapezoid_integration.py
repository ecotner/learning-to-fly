# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 15:16:10 2014

@author: Eric Cotner

Numerical integration program using Simpson's trapezoidal algorithm. Appears to actually
be a bit less precise than the rectangle algorithm, at least for integrating 1/x...
"""

step = 0.000001
x1 = 1
x2 = x1 + step
ans = 0

while (ans < 1):
    ans = ans + step*((1/x2)+(1/x1))/2
    x1 = x1 + step
    x2 = x2 + step
print(x2)