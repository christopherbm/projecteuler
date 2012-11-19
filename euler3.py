"""
Finally works.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import sys
import math

def euler():
	fs = []
	#n = 13195
	n = 600851475143
	s = math.ceil( math.sqrt(n) )
	if(n %2 == 0):
		# 2 is a prime factor
		fs.append(2)
	
	while(n % 2 == 0):
		n = n / 2
		
	f = 3
	cont = True
	while(cont):
		if( n % f == 0 ):
			# f is a factor
			fs.append(f)
			n = n / f
		else:
			f = f + 2
		
		if(f > s):
			cont = False
	
	print fs
			
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