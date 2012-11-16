"""
Warning: Do not run unless you have a really long time to wait for it to complete. Not
fully tested. Works for n=13195.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import sys
import math

def euler():
	n = 600851475143
	# prime factors: 5, 7, 13, 29
	#n = 13195
	
	p = 5
	pm = 0
	finished = False
	while(finished == False):
		if( isPrime(p) ):
			if(p*2 > n):
				finished = True
			
			# on first iteration
			if(pm == 0):
				i = 2 
				while(i != 0):
					res = p * i
					if(res == n):
						# is prime factor
						print p
						pm = i
						i = 0
					elif(res > n):
						# not a factor
						i = 0
					else:
						i = i + 1
			
			# not first iteration
			i = pm
			while(i > 1):
				res = p * i
				if(res == n):
					# is prime factor
					print p
					pm = i
					i = 0
				elif(res < n):
					#not a factor
					i = 0
				else:
					i = i - 1
		
		# increment p by 2 to keep odd
		p = p + 2
		
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
		
	return True

if __name__ == '__main__':
    euler()