# This challenge's submission is broken
# and causes severe run-time issues in the web app.

# The problem has been reported but not fixed.

def is_prime(num):
  	if num == 0 or num == 1: return False
  	for i in range(2, int(num**(1/2.0))+1):
  		if num % i == 0:
  			return False
  	return True

print(is_prime(int(input())))