'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given 'n' scores. Store them in a list and find the score of the runner-up.

Constraints:

2 <= n <= 10
-100 <= A[i] <= 100
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxVal = max(arr)
    arr = filter(lambda x: x != maxVal, arr)
    print (max(arr))
