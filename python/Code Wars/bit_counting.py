'''
Write a function that takes an (unsigned) integer as input, 
and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
'''

def countBits(n):
	# This should've been bin(n).count('1') since bin() returns a string
	# However, didn't realize this at the time.
    return str(bin(n)).count('1')