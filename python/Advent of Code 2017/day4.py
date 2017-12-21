#!/usr/bin/python

'''
Day 3 - Morning (pt. 1)

A new system policy has been put in place that requires all accounts 
to use a passphrase instead of simply a password. 
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
'''

def checkPasses(file):
	content = []
	valids = []
	invalids = []
	skip = False
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	check = content

	while(content):
		phrase = content.pop(0)
		words = phrase.split()
		while(words):
			target = words.pop(0)
			if (target in words):
				skip = True
				break
		if not skip:
			valids.append(phrase)
		else:
			invalids.append(phrase)
		skip = False
	return len(valids)
	
print("\nAnswer: " + str(checkPasses("input/day4.txt")))

'''
Day 3 - Evening (pt. 2)

For added security, yet another system policy has been put in place. 
Now, a valid passphrase must contain no two words that are anagrams of each other - 
that is, a passphrase is invalid if any word's letters can be rearranged to form any 
other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
'''

def checkSortPasses(file):
	content = []
	valids = []
	invalids = []
	skip = False
	with open(file) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	check = content

	while(content):
		phrase = content.pop(0)
		words = phrase.split()
		for i in range(len(words)):
			words[i] = sorted(words[i])
		while(words):
			target = words.pop(0)
			if (target in words):
				skip = True
				break
		if not skip:
			valids.append(phrase)
		else:
			invalids.append(phrase)
		skip = False
	return len(valids)
	
print("\nAnswer: " + str(checkSortPasses("input/day4.txt")))