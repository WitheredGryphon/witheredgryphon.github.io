# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiple_sum(num):
    return sum(x for x in range(num) if not(x % 3 and x % 5))


print (multiple_sum(1000))
