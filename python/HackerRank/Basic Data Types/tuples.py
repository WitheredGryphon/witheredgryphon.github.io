'''
Given an integer, n, and n space-separated integers as input, 
create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''

if __name__ == '__main__':
    n = int(input()) # Unnecessary line of code, but required because of the challenge 
    print(hash(tuple(map(int, input().split(' ')))))