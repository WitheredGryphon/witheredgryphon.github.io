#!/usr/bin/python

''' 
Day 2 - Morning (pt. 1)

The spreadsheet consists of rows of apparently-random numbers. 
To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. 
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
'''

'''numMatrix = [5048,177,5280,5058,4504,3805,5735,220,4362,1809,1521,230,772,1088,178,1794], \
[6629,3839,258,4473,5961,6539,6870,4140,4638,387,7464,229,4173,5706,185,271], \
[5149,2892,5854,2000,256,3995,5250,249,3916,184,2497,210,4601,3955,1110,5340], \
[153,468,550,126,495,142,385,144,165,188,609,182,439,545,608,319], \
[1123,104,567,1098,286,665,1261,107,227,942,1222,128,1001,122,69,139], \
[111,1998,1148,91,1355,90,202,1522,1496,1362,1728,109,2287,918,2217,1138], \
[426,372,489,226,344,431,67,124,120,386,348,153,242,133,112,369], \
[1574,265,144,2490,163,749,3409,3086,154,151,133,990,1002,3168,588,2998], \
[173,192,2269,760,1630,215,966,2692,3855,3550,468,4098,3071,162,329,3648], \
[1984,300,163,5616,4862,586,4884,239,1839,169,5514,4226,5551,3700,216,5912], \
[1749,2062,194,1045,2685,156,3257,1319,3199,2775,211,213,1221,198,2864,2982], \
[273,977,89,198,85,1025,1157,1125,69,94,919,103,1299,998,809,478], \
[1965,6989,230,2025,6290,2901,192,215,4782,6041,6672,7070,7104,207,7451,5071], \
[1261,77,1417,1053,2072,641,74,86,91,1878,1944,2292,1446,689,2315,1379], \
[296,306,1953,3538,248,1579,4326,2178,5021,2529,794,5391,4712,3734,261,4362], \
[2426,192,1764,288,4431,2396,2336,854,2157,216,4392,3972,229,244,4289,1902]'''

def checkSum(num):
	countTotal = 0
	for i in range(0, len(num)):
		numMin = min(num[i])
		numMax = max(num[i])
		countTotal += (numMax - numMin)
		
	return countTotal

#print("\nAnswer: " + str(checkSum(numMatrix)))

'''
Day 2 - Evening (pt. 2)

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

    In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    In the second row, the two numbers are 9 and 3; the result is 3.
    In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
'''

def evenSum(num):
	countTotal = 0
	found = False
	for i in range(0, len(num)):
		for j in range(0, len(num[i])):
			for k in range(0, len(num[i])): # Invoking the almighty O(N^3) taboo
				if num[i][k] != num[i][j]: 
					if num[i][j] % num[i][k] == 0:
						countTotal += num[i][j] / num[i][k]
						break
			#print ("i: " + str(i) + ", " + str(countTotal))
	return countTotal

#print("\nAnswer: " + str(evenSum(numMatrix)))