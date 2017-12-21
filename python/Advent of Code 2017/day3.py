#!/usr/bin/python

''' 
Day 3 - Morning (pt. 1)

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 
and then counting up while spiraling outward. 
For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), 
requested data must be carried back to square 1 (the location of the only access port for this memory system) 
by programs that can only move up, down, left, or right. 
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?


'''

import math

# Adapted from: https://math.stackexchange.com/questions/163080/on-a-two-dimensional-grid-is-there-a-formula-i-can-use-to-spiral-coordinates-in
def getCoords(n):
	k = getRadius(n)
	t = (k * 2) + 1
	m = t ** 2
	t = t - 1
	if n >= (m - t):
		return (k-(m-n), -k)
	else:
		m = m - t
	if n >= (m - t):
		return (-k, -k + (m - n))
	else:
		m = m - t
	if n >= (m - t):
		return (-k + (m - n), k)
	else:
		return (k, k-(m-n-t))
	return (0,0)

def getDist(num):
	coord = getCoords(num)
	return int(abs(coord[0]) + abs(coord[1]))

def getRadius(num):
	rad = int(math.ceil(((num ** (1/2.0)) - 1) / 2))
	return rad

print("\nAnswer: " + str(getDist(1024)))

''' 
Day 3 - Morning (pt. 1)

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
'''
		
def getHigherValue(initNum):
	widthX = getRadius(initNum) * 2
	heightY = getRadius(initNum) * 2
	x = 0
	y = 0
	dx = 0
	dy = -1
	totalVal = 1
	map = []
	
	for i in range(max(widthX, heightY)**2 - 1):
		if -widthX/2 < x <= widthX/2 and -heightY/2 < y <= heightY/2:
			BR = [item for item in map if item[0] == x+1 and item[1] == y-1 and item[3] == True]
			BL = [item for item in map if item[0] == x-1 and item[1] == y-1 and item[3] == True]
			TL = [item for item in map if item[0] == x-1 and item[1] == y+1 and item[3] == True]
			TR = [item for item in map if item[0] == x+1 and item[1] == y+1 and item[3] == True]
			T = [item for item in map if item[0] == x and item[1] == y+1 and item[3] == True]
			B = [item for item in map if item[0] == x and item[1] == y-1 and item[3] == True]
			L = [item for item in map if item[0] == x+1 and item[1] == y and item[3] == True]
			R = [item for item in map if item[0] == x-1 and item[1] == y and item[3] == True]
			if BR:
				totalVal = totalVal + BR[0][2]
			if BL:
				totalVal = totalVal + BL[0][2]
			if TL:
				totalVal = totalVal + TL[0][2]
			if TR:
				totalVal = totalVal + TR[0][2]
			if T:
				totalVal = totalVal + T[0][2]
			if B:
				totalVal = totalVal + B[0][2]
			if L:
				totalVal = totalVal + L[0][2]
			if R:
				totalVal = totalVal + R[0][2]
			map.append((x, y, totalVal, True))
		if totalVal > initNum:
			break
		else:
			if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
				dx, dy = -dy, dx
			x, y = x + dx, y + dy
			totalVal = 0
	
	return totalVal
	
print("\nAnswer: " + str(getHigherValue(277678)))