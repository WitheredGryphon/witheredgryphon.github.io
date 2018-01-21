# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
t = time.time()


def smallest_multiple():
    not_divisible = True
    i = 20

    while not_divisible:
        for j in range(2, 21):
            if i % j:
                break
            if not j % 20 and j == 20 and not i % j:
                not_divisible = False
        if not not_divisible:
            return i
        i += 20


print(smallest_multiple())
print("Time: " + str(time.time()-t))
