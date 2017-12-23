# Challenge 7 - Print Function

# Read an integer N.

# Without using any string methods, try to print the following:
# 123 ... N

# Note that "" represents the values in between,
# such that N=5 would produce the following:
# 12345

if __name__ == '__main__':
	n = int(input())
	for i in range(1, n+1): 
		print (i, end="")