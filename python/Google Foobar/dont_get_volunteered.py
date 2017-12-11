#!/usr/bin/python

# Solar_Doomsday
# Code by: -Redacted for Privacy-
# Adapted BFS Algorithm from: http://www.techiedelight.com/chess-knight-problem-find-shortest-path-source-destination/

'''
Challenge:
To help yourself get to and from your bunk every day, 
write a function called answer(src, dest) which takes in two parameters: the source square, 
on which you start, and the destination square, which is where you need to land to solve the puzzle.  
The function should return an integer representing the smallest number of moves it will take 
for you to travel from the source square to the destination square using a chess knight's moves 
(that is, two squares in any direction immediately followed by one square perpendicular to that direction, 
or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, 
inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
'''
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

class Node:
	def __init__(self, x, y, dist):
		self.x = x
		self.y = y
		self.dist = dist

def to_coordinates(num):
	x = (num) % 8
	y = (num) / 8
	return (x,y)
	
def to_location(num):
	return

def isValid(x, y):
	if (x < 0 or y < 0 or x >= 8 or y >= 8):
		return False
	return True
	
def BreadthFirstSearch(src, dest):
	visited = {}
	queue = []
	initNode = (src, 0)
	queue.append(initNode)
	
	while queue:
		node = queue[0]
		queue.pop(0)
		x = node[0][0]
		y = node[0][1]
		dist = node[1]
		
		if (x == dest[0] and y == dest[1]):
			return dist
				
		if (not any(node == 1 for node in visited)):
			visited[node] = True;
			
			for i in range(0, 8):
				x1 = x + row[i]
				y1 = y + col[i]
				
				if (isValid(x1, y1)):
					newNode = ((x1, y1), dist + 1)
					queue.append(newNode)
					
	return

def answer(src, dest):

	src_coords = to_coordinates(src)
	dest_coords = to_coordinates(dest)
		
	return BreadthFirstSearch(src,dest)