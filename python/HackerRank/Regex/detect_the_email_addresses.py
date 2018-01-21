'''
You will be provided with a block of text, spanning not more than hundred lines. 
Your task is to find the unique e-mail addresses present in the text. 
You could use Regular Expressions to simplify your task. 
And remember that the "@" sign can be used for a variety of purposes!

Input Format

The first line contains an integer N (N<=100), which is the number of lines present in the text fragment which follows.
From the second line, begins the text fragment (of N lines) in which you need to search for e-mail addresses.

Output Format

All the unique e-mail addresses detected by you, in one line, in lexicographical order, with a semi-colon as the delimiter. 
'''

import re

matches = []

for i in range(int(input())):
    match = re.findall("\\b(?:\w|\.){1,}@(?:\w*\.*){1,}\\b", input())
    matches.extend(match)
matches = (list(filter(None,matches)))
matches = ';'.join(sorted(set(filter(None, matches))))
print (matches)