# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import time
t = time.time()

palindrome_appendix = []


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def number_brute_force():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if is_palindrome(product):
                palindrome_appendix.append(product)


number_brute_force()
print("Time: " + str(time.time()-t))
print("Answer: " + str(max(palindrome_appendix)))
