# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:01:02 2017

Script for generating solutions to the game "Four fours".

THE GAME: The object of the game is to generate as many of the positive integers (in order) as possible,
using only four fours and a selected set of mathematical functions (such as addition, multiplication,
factorial, exponentiation, etc).
Example:
    0 = (4+4)-(4+4)
    1 = (4/4)*(4/4)
    2 = (4*4)/(4+4)
    etc...

THE THEORY: Each allowed function can be divided into two subsets: unary and binary. Unary functions take
a single argument and return a single number. Binary functions take two arguments and return a single
number. Therefore, any valid expression must contain 3 binary functions (the # of 4's used is #binary+1)
and any number of unary functions. Once we have constructed an expression containing 3 binary functions,
it is a valid expression and may be evaluated. Whether it is the one we are looking for is not so sure...

THE ALGORITHM: The algorithm for solving this problem involves the generation of successive dictionaries
containing expressions that make use of one 4, two 4's, three 4's, and finally four 4's. To construct
the first dictionary (expressions with one 4), we start simply with the number 4, and then repeatedly
apply all unary operators to it. Any time an expression evaluates to a number that is not in the dictionary,
we add it to the dictionary. We also set a limit on the max number of unary functions that can be applied,
and the maximum value that we will keep in our dictionary (repeated factorials become astronomically
large after a short time). Once this is done, our first dictionary is complete. Then, to construct the
second dictionary (expressions containing two 4's), we apply all binary functions to all possible
combinations of expressions from the first dictionary, saving new values. We then apply all unary
functions to these expressions, also saving new values. Then we build the third dictionary in the same
way, using all pairs of the first and second dictionary (1+2=3), and finally the fourth dictionary
using all the previous dictionaries (1+3=2+2=4). Then, we simply list the keys and associated expressions
of the fourth dictionary in numerical order.
This algorithm can easily be generalized to numbers other than 4 (five 5's, six 6's, etc.), as has been
done in the script.

@author: 27182_000
"""

# import important modules for special functions
import math as m
import scipy as sp

# global variables important for the running of the algorithm
FOUR = 4                    # the most important number - it determines that we're playing 4 4's (could be modified so that we're playing 3 3's, 5 5's, etc.)
MAXVALUE = 5*10**3            # maximum value to be stored in hash tables/dictionaries (repeated factorials can quickly produce astronomically large numbers)
EPSILON = 10**-4            # if floats are produced by the calculations, and they are within <EPSILON> of the closest integer, it just rounds them
ROUNDING_LEVEL = 6          # the digits of rounding to be used on floats (only relevant if not requiring values at each step)
MAXUNARY = 3                # maximum number of unary functions to apply between each application of binary functions
NUMTOPRINT = MAXVALUE       # number of entries in the final table to print

# initialize list of empty dictionaries (except for initial value <FOUR>)
dictList = [{} for i in range(FOUR)]
dictList[0][FOUR] = str(FOUR)
# define the usable functions and their string representations
unaryFunc = {'fact': lambda x: m.factorial(x),                          # factorial
             'dfact': lambda x: sp.misc.factorial2(x, exact=True),      # double factorial
             'gamma': lambda x: sp.special.gamma(x),                    # gamma function
             'sqrt': lambda x: m.sqrt(x)}                               # square root
unaryFuncStr = {'fact': lambda x: '(' + str(x) + '!)',
                'dfact': lambda x: '(' + str(x) + '!!)',
                'gamma': lambda x: '\u0393(' + str(x) + ')',
                'sqrt': lambda x: '\u221a(' + str(x) + ')'}
binaryFunc = {'add': lambda x,y: x+y,                                   # addition
              'sub': lambda x,y: x-y,                                   # subtraction
              'mult': lambda x,y: x*y,                                  # multiplication
              'div': lambda x,y: x/y,                                   # division
              'exp': lambda x,y: x**y,                                  # exponentiation
              'con': lambda x,y: int(str(x) + str(y)),                  # string concatenation
              'binom': lambda x,y: sp.special.binom(x,y)}               # binomial coefficient
binaryFuncStr = {'add': lambda x,y: '(' + str(x) + '+' + str(y) + ')',
                 'sub': lambda x,y: '(' + str(x) + '-' + str(y) + ')',
                 'mult': lambda x,y: '(' + str(x) + '*' + str(y) + ')',
                 'div': lambda x,y: '(' + str(x) + '/' + str(y) + ')',
                 'exp': lambda x,y: '(' + str(x) + '^' + str(y) + ')',
                 'con': lambda x,y: '(\'' + str(x) + '\'+\'' + str(y) + '\')',
                 'binom': lambda x,y: '(' + str(x) + 'C' + str(y) + ')'}

# define function for rounding results, keeping floats as floats, but converting floats within <EPSILON> of an integer into integers
def roundResult(result):
    integer_part = round(result)
    if abs(result - integer_part) <= EPSILON:
        return int(integer_part)
#    else:
#        return float(round(result, ROUNDING_LEVEL))

# define function for applying unary operators to each expression in a dictionary
def applyUnary(Dict):
    # define recursive helper function
    def applyUnaryRecursive(dictionary, nUnary):
        dictKeys = list(dictionary.keys())
        # for every value in the dictionary
        for value in dictKeys:
            # for each possible unary function
            for func in unaryFunc:
                try:
                    # apply function to each available expression in dictionary
                    result = unaryFunc[func](value)
                    result = roundResult(result)
                    # add new expression to dictionary (if value less than some max value and not already in dictionary)
                    if abs(result) <= MAXVALUE:
                        if result not in dictionary:
                            dictionary[result] = unaryFuncStr[func](dictionary[value])
                # if any of the expressions returns an error, just discard it
                except:
                    pass
        nUnary += 1
        # apply function recursively on the updated dictionary (if number of unary functions has not exceeded some number)
        if nUnary < MAXUNARY:
            applyUnaryRecursive(dictionary, nUnary)
    # call the recursive function
    applyUnaryRecursive(Dict, 0)

# define function for applying binary operators to each pair of expressions in a dictionary
def applyBinary(dict1, dict2):
    dict1Keys = list(dict1.keys())
    dict2Keys = list(dict2.keys())
    newDict = {}
    # iterate over each pair of elements in the dictionary
    for val1 in dict1Keys:
        for val2 in dict2Keys:
            # iterate over all binary functions
            for func in binaryFunc:
                try:
                    # apply function to each available pair of expressions in dictionary
                    result = binaryFunc[func](val1, val2)
                    result = roundResult(result)
                    # add new expression to dictionary (if less thena max value and not already in dictionary)
                    if abs(result) <= MAXVALUE:
                        if result not in newDict:
                            newDict[result] = binaryFuncStr[func](dict1[val1], dict2[val2])
                # if any expressions returns an error, discard it
                except:
                    pass
    return newDict

# generate dictionary with all expressions built with a single number
applyUnary(dictList[0])
# generate dictionary with all expressions built from n numbers, given the dictionary for <n numbers
# want to combine the n-1 and 1 dictionaries, (n-2, 2), (n-3, 3), ... (floor(n/2), ceiling(n/2))
for n1 in range(1, FOUR):
    for n2 in range(n1):
        newDict = applyBinary(dictList[n2], dictList[n1-n2-1])
        for val in newDict:
            if val not in dictList[n1]:
                dictList[n1][val] = newDict[val]
#        dictList[n1].update(newDict)
    applyUnary(dictList[n1])
# return the final dictionary built from all <FOUR> numbers
for i in range(NUMTOPRINT+1):
    try:
        print('{0} = {1}'.format(i, dictList[FOUR-1][i]))   # use .get(i) to skip entries that don't exist in the dictionary
    except KeyError:
        print('\tCan\'t compute expression for {}.'.format(i))





