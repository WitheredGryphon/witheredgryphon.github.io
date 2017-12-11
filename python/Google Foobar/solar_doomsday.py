#!/usr/bin/python

# Solar_Doomsday
# Code by: Christian Medina

# Credit for Algorithms: DaniWeb, Wikipedia

# Digit-By-Digit isqrt recursion
# https://en.wikipedia.org/wiki/Integer_square_root
def isqrt(n):
	if (n < 0):
		return
	elif (n < 2):
		return n
	else:
		small = isqrt(n >> 2) << 1
		large = small + 1
		if (large * large) > n:
			return small
		else:
			return large

# Prime function utilizing no math import
# goo.gl/YmCR78
def isPrime(n):
    n = abs(int(n))

    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

# Primary function
def answer(area):
	squareList = []
	while(area >= 1):
		simp = isqrt(area)**2
		if (isPrime(simp)):				# End-of-chain, append prime numbers
			squareList.append(simp)
			break
		if (area == simp):				# One big square, immediately solved
			squareList.append(simp)
			break
		area -= simp					# Continue decrementing and appending as necessary
		squareList.append(simp)
	return squareList