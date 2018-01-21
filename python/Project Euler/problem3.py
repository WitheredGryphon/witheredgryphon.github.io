def prime_factorization(num):
    factors = []

    for i in range(2, int(num ** 0.5)):
        while num % i == 0:
            factors.append(i)
            num /= i
    return factors


print(prime_factorization(600851475143))

