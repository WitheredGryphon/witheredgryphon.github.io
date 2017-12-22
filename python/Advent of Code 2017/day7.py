#!/usr/bin/python 

class Node:
	weight = 0
	name = ""
	parent = ""
	children = ""
	
	def __init__(self, weight, name, parent, children):
		self.weight = weight
		self.name = name
		self.parent = parent
		self.children = children
		
def recursiveCircus(file):
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	nodes = []
	print content
	
	for i in range(0, len(content))
		#weight = 
	
recursiveCircus("input/day7_sample.txt")