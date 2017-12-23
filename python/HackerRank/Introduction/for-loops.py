# Challenge 5 - For-Loops

# Read an integer n. For all non-negative integers i < N, print i^2.

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i ** 2)