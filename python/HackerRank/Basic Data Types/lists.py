'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each 
command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
	N = int(input())
	numList = []
	printQueue = []
	for i in range(0, N):
		cmd = input()
		cmdList = cmd.split(' ')
		if len(cmdList) > 2:
			cmdList[1] = int(cmdList[1])
			cmdList[2] = int(cmdList[2])
		if len(cmdList) > 1:
			cmdList[1] = int(cmdList[1])
		if cmdList[0] == 'insert':
			cmdList[2] = int(cmdList[2])
			while len(numList) < cmdList[1]:
				numList.append(0)
			numList.insert(cmdList[1], cmdList[2])
		elif cmdList[0] == 'print':
			printCopy = numList[:]
			printQueue.append(printCopy)
		elif cmdList[0] == 'remove':
			del numList[numList.index(cmdList[1])]
		elif cmdList[0] == 'append':
			numList.append(cmdList[1])
		elif cmdList[0] == 'sort':
			numList = sorted(map(int, numList))
		elif cmdList[0] == 'pop':
			numList.pop()
		elif cmdList[0] == 'reverse':
			numList.reverse()
	print("\nAnswer: ")
	for k in printQueue:
		print(k)