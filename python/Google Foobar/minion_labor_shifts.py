#!/usr/bin/python

# Solar_Doomsday
# Code by: -Redacted for Privacy-

# Challenge: Write a function called answer(data, n) that takes in a list of 
# less than 100 integers and a number n, and returns that same list but with 
# all of the numbers that occur more than n times removed entirely. 
# The returned list should retain the same ordering as the original list -
# you don't want to mix up those carefully-planned shift rotations! For instance, 
# if data was [5, 10, 15, 10, 7] and n was 1, 
# answer(data, n) would return the list [5, 15, 7] because 10 occurs twice, 
# and thus was removed from the list entirely.

def answer(data,n):
	returnList = []
	count = 0
	for i in range(len(data)):
		if (data.count(data[i]) <= n): 					# Check if the count of occurences < n
			returnList.append(data[i])					# Append to the answer list
		else:
			list(filter(lambda x: x != data[i], data)) 	# Filter all occurences of data[i]
	
	return returnList