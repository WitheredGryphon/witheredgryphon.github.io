'''
Day 18 - Morning (pt. 1)

It seems like the assembly is meant to operate on a set of registers that are each named with a single letter and that can each hold a single integer. 
You suppose each register should start with a value of 0.

There aren't that many instructions, so it shouldn't be hard to figure out what they do. 

Here's what you determine:

snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y 
(that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. 
(If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. 
(An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Many of the instructions can take either a register (a single letter) or a number. 
The value of a register is the integer it contains; the value of a number is that number.

After each jump instruction, the program continues with the instruction to which the jump jumped. 
After any other instruction, the program continues with the next instruction. 
Continuing (or jumping) off either end of the program terminates it.

For example:

set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2

The first four instructions set a to 1, add 2 to it, square it, and then set it to itself modulo 5, resulting in a value of 4.
Then, a sound with frequency 4 (the value of a) is played.
After that, a is set to 0, causing the subsequent rcv and jgz instructions to both be skipped 
(rcv because a is 0, and jgz because a is not greater than 0).
Finally, a is set to 1, causing the next jgz instruction to activate, jumping back two instructions to another jump, 
which jumps again to the rcv, which ultimately triggers the recover operation.
At the time the recover operation is executed, the frequency of the last sound played is 4.

What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?
'''

import re

duetOneQueue = []
duetTwoQueue = []

def duetOne(file, vals):
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	
	freqVal = 0
	registers = []
	
	for i in range(0, len(content)):
		match = re.search("(?:^\w{3})(?:\s{1})(\w*)", content[i])
		if [match.group(1), 0] not in registers:
			registers.append([match.group(1), 0])
	
	i = 0
	
	while i < len(content):
		match = re.search("(^\w{3})(?:\s{1})(\w*)(?:\s{0,1})(\W?\d+|[a-z])", content[i])
		instruction = match.group(1)
		register = match.group(2)
		value = 0
		inc = False
		if len(content[i]) > 2:
			value = match.group(3)
			
		if instruction == "set":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric():
				matchReg[0][1] = int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] = int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "mul":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] *= int(value)
			else:
				targetReg = [item for item in registers if item[0] == str(value)]
				matchReg[0][1] *= int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "jgz":
			if not value.isnumeric():
				matchReg = [item for item in registers if item[0] == register]
				if int(matchReg[0][1]) > 0:
					i += int(value)
					inc = True
			else:
				if int(value) > 0:
					i += int(value)
					inc = True
		elif instruction == "add":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] += int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] += int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "mod":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] %= int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] %= int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "rcv":
			# Witch craft goes here
		elif instruction == "snd":
			# Black magic goes here
		print(str(instruction) + " " + str(register) + " " + str(value))
		print(registers)
		print("\n")
		if not inc:
			i += 1
	return freqVal
	
def duetTwo(registers, vals):
	
	for i in range(0, len(content)):
		match = re.search("(?:^\w{3})(?:\s{1})(\w*)", content[i])
		if [match.group(1), 0] not in registers:
			registers.append([match.group(1), 0])
	
	i = 0
	
	while i < len(content):
		match = re.search("(^\w{3})(?:\s{1})(\w*)(?:\s{0,1})(\W?\d+|[a-z])", content[i])
		instruction = match.group(1)
		register = match.group(2)
		value = 0
		inc = False
		if len(content[i]) > 2:
			value = match.group(3)
			
		if instruction == "set":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric():
				matchReg[0][1] = int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] = int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "mul":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] *= int(value)
			else:
				targetReg = [item for item in registers if item[0] == str(value)]
				matchReg[0][1] *= int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "jgz":
			if not value.isnumeric():
				matchReg = [item for item in registers if item[0] == register]
				if int(matchReg[0][1]) > 0:
					i += int(value)
					inc = True
			else:
				if int(value) > 0:
					i += int(value)
					inc = True
		elif instruction == "add":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] += int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] += int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "mod":
			matchReg = [item for item in registers if item[0] == register]
			matchIndex = registers.index([matchReg[0][0], matchReg[0][1]])
			if value.isnumeric() or value[:1] == "-":
				matchReg[0][1] %= int(value)
			else:
				targetReg = [item for item in registers if item[0] == value]
				matchReg[0][1] %= int(targetReg[0][1])
			registers[matchIndex] = matchReg[0]
		elif instruction == "rcv":
			# Wizardry here
		elif instruction == "snd":
			# Sorcery goes here
		print(str(instruction) + " " + str(register) + " " + str(value))
		print(registers)
		print("\n")
		if not inc:
			i += 1
	return freqVal

print (duet("input/day18.txt"))