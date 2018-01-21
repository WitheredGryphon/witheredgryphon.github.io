def iter_fib():
    x = 0
    y = 1
    t = 0
    while x < 4000000:
        if not(x % 2):
            t += x
        x, y = y, y + x
    return t


print(iter_fib())
