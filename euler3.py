def euler():
	n = 600851475143
	# prime factors: 5, 7, 13, 29
	#n = 13195
	answers = []
	factors = doFactor(n)
	for f in factors:
		g = doFactor(f)
		if len(g) == 0:
			answers.append(f)
			
	print answers
		
def doFactor(n):
	l = []
	i = 2
	while i < n:
		if n % i == 0:
			l.append(i)
		i = i + 1
	
	return l
	

if __name__ == '__main__':
    euler()