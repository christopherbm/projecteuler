"""
Warning: Do not run unless you have a really long time to wait for it to complete. Not
fully tested. Works for n=13195.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

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
	
def isPrime(n):
	if(n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
		return False
		
	s = math.ceil( math.sqrt(n) )
	while( s > 1 ):
		if n % s == 0:
			return False
		s = s - 1

if __name__ == '__main__':
    euler()