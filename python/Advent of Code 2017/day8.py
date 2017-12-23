#!/usr/bin/python

'''
Day 8 - Morning (pt. 1)


You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, 
it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: 
the register to modify, whether to increase or decrease that register's value, 
the amount by which to increase or decrease it, and a condition. 
If the condition fails, skip the instruction without modifying the register. 

* The registers all start at 0. *

The instructions look like this: 

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). 
However, the CPU doesn't have the bandwidth to tell you what all the registers are named, 
and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?
'''

import re

def strangeRegisters(file, findHighest):
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	
	registers = []
	highVal = 0
	
	# Populate the registers list so we can modify them later
	# Also need to avoid duplicates which the REGEX grabs
	for k in range (0, len(content)):
		match = re.search("(^[a-z]{1,3})", content[k])
		if [match.group(0), 0] not in registers:
			registers.append([match.group(0), 0]) # Initialize all registers to 0
			
	#print(registers)
		
	for i in range(0, len(content)):
		# REGEX (again)
		match = re.search("(^[a-z]{1,3})(?:\s{1})([inc|dec]{3})(?:\s{1})(\W?\d+)(?:\s{1}\S{2}\s{1})([a-z]{1,3})(?:\s{1})(\W{1,2})(?:\s{1})(\W?\d+)", content[i])
		# Group 0 contains the full match of all the groups (which is just the full string)
		register = match.group(1)
		instruction = match.group(2)
		insValue = match.group(3)
		target = match.group(4)
		operator = match.group(5)
		conditional = match.group(6)
		val = int(insValue)
		conditional = int(conditional)
		
		if operator == '>':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]]) # Might be redundant to do this, just a precaution
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			
			if (op2Val > conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		elif operator == '>=':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]])
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			op1Val = int(op1[0][1])
			if (op2Val >= conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		elif operator == '<':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]])
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			
			if (op2Val < conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		elif operator == '<=':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]])
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			
			if (op2Val <= conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		elif operator == '==':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]])
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			
			if (op2Val == conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		elif operator == '!=':
			op1 = [item for item in registers if item[0] == register]
			op1Index = registers.index([op1[0][0], op1[0][1]])
			op2 = [item for item in registers if item[0] == target]
			op2Index = registers.index([op2[0][0], op2[0][1]])
			op2Val = int(op2[0][1])
			
			if (op2Val != conditional):
				if instruction == "inc":
					op1[0][1] = int(op1[0][1]) + val
				else:
					op1[0][1] = int(op1[0][1]) - val
			registers[op1Index][1] = op1[0][1]

		checkVal = max(registers, key=lambda x:x[1])
		if checkVal[1] > highVal:
			highVal = checkVal[1]
		
	if findHighest:
		return highVal
	else:
		return max(registers, key=lambda x:x[1])
	
'''
Day 8 - Evening (pt. 2)

To be safe, the CPU also needs to know the highest value held in any register 
during this process so that it can decide how much memory to allocate to these operations. 

For example, in the above instructions, 
the highest value ever held was 10 (in register c after the third instruction was evaluated).
'''

# NOTE: PART 1's ANSWER CAN BE RETRIEVED BY CHANGING "True" TO "False" IN THE FUNCTION CALL
print("\nAnswer: " + str(strangeRegisters("input/day8.txt", True)))
