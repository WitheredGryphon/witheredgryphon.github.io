def convertToBase(n, b):
	m = []
	while n > 0:
		d = int(n / b)
		r = n % b
		n = d
		m.insert(0,r)
	s = ''.join(map(str, m))
	s = int(s)
	return s

def convertFromBase(num, b):
	n = len(str(num)) - 1
	s = 0
	i = 0
	digits = [int(d) for d in str(num)]
	while n >= 0:
		s += digits[i] * (b**n)
		n -= 1
		i += 1
	return s

def answer(n, b):
	num = n
	if(b != 10):
		num = convertFromBase(n, b)
	
	
	k = len(str(num))
	digits = [int(d) for d in str(num)]
	x = sorted(digits, reverse=True)
	x = ''.join(map(str,x))
	x = int(x)
	y = sorted(digits)
	y = ''.join(map(str,y))
	y = int(y)
	z = x - y
	prevNum = convertToBase(z, b)
	print(x)
	print(y)
	print(z)
	print(convertToBase(z, b))
	
	
answer(210022, 3)