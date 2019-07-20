"""
Solves the knapsack problem using memoization (dynamic programming).
"""

def knapsack(weights, values, capacity):
    ''' Function for solving knapsack problem. Returns value of optimal knapsack. '''

    # Define dict for memoization:
    K = {}

    # Build dict from the bottom up:
    for i in range(len(weights)+1):
        for w in range(capacity+1):
            # Base case:
            if (i==0) or (w==0):
                K[(i,w)] = 0
            # Value of knapsack at level i and weight w is max of value with item i and without
            elif (weights[i-1] <= w):
                K[(i,w)] = max(K[(i-1,w-weights[i-1])] + values[i-1], K[(i-1,w)])
            # Otherwise can't fit item into bag
            else:
                K[(i,w)] = K[(i-1,w)]

    return K[(len(weights),capacity)]

weights = [1,1,2,3,2,1,1,4,5,1]
values =  [1,2,3,3,3,1,1,1,5,2]
capacity = 2
print(knapsack(weights, values, capacity))
