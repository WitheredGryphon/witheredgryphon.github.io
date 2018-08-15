'''
Day 12

You walk through the village and record the ID of each program and the IDs 
with which it can communicate directly (your puzzle input). 
Each program has one or more programs with which it can communicate, 
and these pipes are bidirectional; if 8 says it can communicate with 11, 
then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?
'''

import re

def digitalPlumber(file):
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	
	relatives = []
	nonrelatives = [] # Sort twice to catch any missed relatives
	
	for i in range(0, len(content)):
		match = re.search("(^\d+)(?:\s{1}\W{3}\s{1})([\d+\W?\s?]+)", content[i])
		parent = match.group(1)
		children = match.group(2)
		children = children.split(', ')
		
		if parent == '0':
			relatives.append(parent)
		if '0' in children:
			for k in children:
				if not k in relatives: 
					relatives.append(k)
		for j in children:
			if j in relatives and parent not in relatives:
				relatives.append(parent)
		if parent not in relatives:
			nonrelatives.append(match.group(0))
	
	iter = 0
	loopCounter = 0
	while(nonrelatives):
		copyNonRelatives = nonrelatives[:]
		match = re.search("(^\d+)(?:\s{1}\W{3}\s{1})([\d+\W?\s?]+)", nonrelatives[iter])
		parent = match.group(1)
		children = match.group(2)
		children = children.split(', ')
		deleter = False
		
		for j in children:
			#print("* Child: " + str(j))
			#print("* Parent: " + str(parent))
			if j in relatives and parent not in relatives:
				relatives.append(parent)
				deleter = True
			if deleter:
				del nonrelatives[iter]
		
		if iter >= len(nonrelatives) - 1:
			iter = 0
		else:
			iter += 1
			
		if copyNonRelatives == nonrelatives:
			loopCounter += 1
		else:
			loopCounter = 0
		#print (loopCounter)
		if loopCounter > 20000:
			break
		#print (relatives)
		#print ("---")
		#print (nonrelatives)
		#print ("\n")
	return relatives
	
lst = digitalPlumber("input/day12.txt")
lst = sorted(lst)
print("\nAnswer: " + str(len(lst)))