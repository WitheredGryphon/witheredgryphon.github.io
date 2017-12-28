'''
Given an integer, , print the following values for each integer i from 1 to n:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of n.
'''

def print_formatted(number):
    width = int(len(str(bin(number))[2:])+1)
    for i in range(1,number+1):
        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        b = str(bin(i))[2:]
        d = str(i)
        print(" "*(width-len(d)-1) + str(i) + " "*(width-len(o)) + str(oct(i))[2:] + " "*(width-len(h)) + str(hex(i))[2:].upper() + " "*(width-len(b)) + str(bin(i)[2:]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)