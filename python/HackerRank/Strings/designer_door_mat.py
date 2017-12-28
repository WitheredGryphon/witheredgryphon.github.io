'''
Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

    Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format

A single line containing the space separated values of N and M.
'''

# More than 6 lines of code will result in 0 score. Blank lines are not counted.
N, M = map(int,input().split())
for i in range(1,N,2): 
    print (("-"*((M-(i*3))//2)) + (".|."*i) + ("-"*((M-(i*3))//2)))
print ("-"*((M-7)//2)+"WELCOME"+"-"*((M-7)//2))
for i in range(N-2,-1,-2): 
    print (("-"*((M-(i*3))//2)) + (".|."*i) + ("-"*((M-(i*3))//2)))
