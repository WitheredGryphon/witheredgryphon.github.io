#!/usr/bin/python

n = 15 # damage
c = 99 # coins
i = 0

while i < c:
	n += (n * 0.0125)
	i += 1;

print(n)
