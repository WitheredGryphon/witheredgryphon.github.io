'''
Write a function, persistence, 
that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
'''

# Dev note: reduce was moved in Python 3 and has to be separately imported
# However, the challenge only supported Python 2

from operator import mul

def persistence(n):
    total = 0
    strN = map(int, str(n))
    while len(strN) > 1:
        total += 1
        n = reduce(mul, strN, 1)
        strN = map(int, str(n))
    return total