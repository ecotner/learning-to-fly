# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:41:29 2017

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used? 

@author: 27182_000
"""

numToWords = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
              11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
              18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
              80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

total = 0

#iterate through all the numbers
for num in range(1,1000+1):
    #start new word each pass
    word = ''
    #split into cases: num >= 100, 20 <= num <= 99, 10 <= num <= 19, and everything else
    #if num >= 100, find divisor of 100, then add "_divisor hundred and" to word
    if num >= 1000:
        if num % 1000 == 0:
            word += numToWords[int(num/1000)] + 'thousand'
            num = 0
        else:
            word += numToWords[int(num/1000)] + 'thousand'
            num %= 1000 
    if 100 <= num <= 999:
        if num % 100 == 0:
            word += numToWords[int(num/100)] + 'hundred'
            num = 0
        else:
            word += numToWords[int(num/100)] + 'hundredand'
            num %= 100
    if 20 <= num <= 99:
        word += numToWords[10*int(num/10)] + numToWords[num % 10]
        num = 0
    elif 1 <= num <= 19:
        word += numToWords[num]
    total += len(word)
print total
print word