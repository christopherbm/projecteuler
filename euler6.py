"""Question: 
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 100 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
"""

def euler():
	r = range(1, 101)
	def f(x): return x*x
	s1 = sum( map(f, r) )
	
	s2 = f( sum( range(1,101) ) )
	
	print s2 - s1

if __name__ == '__main__':
    euler()