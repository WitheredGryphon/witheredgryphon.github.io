#!/usr/bin/python

''' 
Day 1 - Morning (pt. 1)

The captcha requires you to review a sequence of digits (your puzzle input) and 
find the sum of all digits that match the next digit in the list. 
The list is circular, so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
'''

def sumCaptcha(num):
	captchaTotal = 0

	if num[0] == num[-1]:
		captchaTotal = captchaTotal + int(num[0])
	
	for i in range(1, len(num)):
		intNum = int(num[i])
		if intNum == int(num[i-1]):
			captchaTotal = captchaTotal + intNum
	
	return captchaTotal

#number = str(input("Enter a number:"))
#print("\nAnswer: " + str(sumCaptcha(number)))

''' 
Day 1 - Evening (pt. 2)

Now, instead of considering the next digit, 
it wants you to consider the digit halfway around the circular list. 
That is, if your list contains 10 items, only include a digit in your sum 
if the digit 10/2 = 5 steps forward matches it. 
Fortunately, your list has an even number of elements.

For example:

    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
    1221 produces 0, because every comparison is between a 1 and a 2.
    123425 produces 4, because both 2s match each other, but no other digit has a match.
    123123 produces 12.
    12131415 produces 4.

What is the solution to your new captcha?
'''

def halfSumCaptcha(num):
	captchaTotal = 0
	parseFull = int(len(num))
	step = parseFull/2
	
	num += num
	print(str(num))
	
	for i in range(0, len(num)/2):
		intNum = int(num[i])
		if intNum == int(num[(i) + step]):
			captchaTotal = captchaTotal + intNum
	
	return captchaTotal

#number = str(input("Enter a number:"))
#print("\nAnswer: " + str(halfSumCaptcha(number)))