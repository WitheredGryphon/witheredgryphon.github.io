# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

# Dev note: utilizing Miller–Rabin primality test
# See: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python (<-- code errors are listed in the primality
# test that have been corrected here)
#
# This primality test is probabilistic, and as a result the answer may not always be accurate.
# Would not recommend this for prime sets of 1 million or more as sieving is far more efficient at that point

from random import *
import time

t = time.time()


def is_composite(a, d, n, r):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(r):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True


def is_prime(n, tests):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    r = 0
    d = n - 1

    while d:
        qu, re = divmod(d, 2)
        if re:
            break
        r += 1
        d = qu

    if 2 ** r * d != n - 1:
        return False

    for i in range(tests):
        a = randint(2, n - 2)
        if is_composite(a, d, n, r):
            return False
    return True


def fill_primes():
    primes = []
    i = 2
    while len(primes) < 1000000:
        k = 5   # increase for higher accuracy, default to 5
        if is_prime(i, k):
            primes.append(i)
        i += 1
    return primes[-1]


print(fill_primes())
print("Time: " + str(time.time()-t) + "\n")

t = time.time()
