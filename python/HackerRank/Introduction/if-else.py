# Challenge 2 - If-Else

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input()) # raw_input() for Python 2
    if n % 2 == 1 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")