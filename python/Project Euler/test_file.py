# This file is entirely used for testing purposes
# The contents within it were not created by me

n = 1000
i = 2

for i in range(2, n+1):
    if (n % i == 0):
        n = n / i
        print(i)