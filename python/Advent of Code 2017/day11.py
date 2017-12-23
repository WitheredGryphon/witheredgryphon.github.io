'''
Day 11

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the 
north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
  
You have the path the child process took. 
Starting where he started, you need to determine the fewest number of steps required to reach him. 
(A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
'''

def getSteps(file):
	steps = 0
	
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	content = str(content[0])
	directions = content.split(',')
	dists = []
	x = 0
	y = 0
	z = 0
	
	for i in directions:
		if i == "n":
			y += 1
			z -= 1
		elif i == "ne":
			x += 1
			z -= 1
		elif i == "nw":
			x -= 1
			y += 1
		elif i == 's':
			y -= 1
			z += 1
		elif i == 'se':
			x += 1
			y -= 1
		elif i == 'sw':
			x -= 1
			z += 1
		distance = (abs(x) + abs(y) + abs(z)) / 2
		dists.append(distance)

	print ("\nAnswer: " + str((abs(x) + abs(y) + abs(z)) / 2))
	return max(dists)

# Red Blob on Hex Grid Navigation, Dists, etc.:
# https://www.redblobgames.com/grids/hexagons/
	
print ("\nAnswer: " + str(getSteps("input/day11.txt")))