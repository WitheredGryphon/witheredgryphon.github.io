'''
You are given a string S.

Your task is to find out if the string S contains: 
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 
'''

if __name__ == '__main__':
    s = input()
    print(any(str.isalnum(c) for c in s))
    print(any(str.isalpha(c) for c in s))
    print(any(str.isdigit(c) for c in s))
    print(any(str.islower(c) for c in s))
    print(any(str.isupper(c) for c in s))