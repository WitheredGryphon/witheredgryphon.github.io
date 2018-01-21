def multiple_sum(num):
    return sum(x for x in range(num) if not(x % 3 and x % 5))


print (multiple_sum(1000))
