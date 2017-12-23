'''
Day 23 - Morning (pt. 1)

The code it's running seems to be a variant of the kind you saw recently on that tablet (day 18). 
The general functionality seems very similar, but some of the instructions are different:

set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. 
(An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, 
which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?
'''

import re

def coprocessorConflagration(file):
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	
	registers = [["a", 0], ['b', 0], ["c", 0], ["d", 0], ["e", 0], ["f", 0], ["g", 0], ["h", 0]]
	i = 0
	
	while i < len(content):
		match = re.search("(^[a-z]{3})(?:\s{1})(1|[a-z])(?:\s{1})(\W?\d+|[a-z])", content[i])
		
		instruction = match.group(1)
		location = match.group(2)
		value = match.group(3)
		inc = False
		
		if instruction == "set":
			register = [item for item in registers if item[0] == location]
			registerIndex = registers.index([register[0][0], register[0][1]])
			if value.isnumeric() or value[:1] == "-":
				value = int(value)
				registers[registerIndex][1] = int(value)
			else:
				targetRegister = [item for item in registers if item[0] == value]
				registers[registerIndex][1] = targetRegister[0][1]
		elif instruction == "jnz":
			if not location.isnumeric():
				register = [item for item in registers if item[0] == location]
				if int(register[0][1]) != 0:
					i += int(value)
					inc = True
			else:
				if int(location) != 0:
					i += int(value)
					inc = True
		elif instruction == "mul":
			register = [item for item in registers if item[0] == location]
			registerIndex = registers.index([register[0][0], register[0][1]])
			if value.isnumeric() or value[:1] == "-":
				value = int(value)
				registers[registerIndex][1] *= int(value)
			else:
				targetRegister = [item for item in registers if item[0] == value]
				registers[registerIndex][1] *= targetRegister[0][1]
		elif instruction == "sub":
			register = [item for item in registers if item[0] == location]
			registerIndex = registers.index([register[0][0], register[0][1]])
			if value.isnumeric() or value[:1] == "-":
				value = int(value)
				registers[registerIndex][1] -= int(value)
			else:
				targetRegister = [item for item in registers if item[0] == value]
				registers[registerIndex][1] -= targetRegister[0][1]
		if not inc:
			i += 1
		#print (registers)
	return registers[-1][1]
		
print("\nAnswer: " + str(coprocessorConflagration("input/day23.txt")))

'''
Day 23 - Evening (pt. 2)

The debug mode switch is wired directly to register a. 
You flip the switch, which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. 
Whoever wrote this program obviously didn't choose a very efficient implementation. 
You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. 
Technically, if it had that... it wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion, 
what value would be left in register h?
'''

def simulation():
	b = 109900
	c = 126900
	h = 0
	# ^^^ all initialized through the assembly, unique to each user
	
	for i in range(b, c+1, 17): # b increases by 17
		for k in range (2, i): # check for values between [2, i] that are composite
			if i % k == 0:
				h += 1 # increase by 1 for composites
				break
	return h

print("\nAnswer: " + str(simulation()))