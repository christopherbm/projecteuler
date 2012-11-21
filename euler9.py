"""Question: 
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 3*3 + 4*4 = 9 + 16 = 25 = 5*5.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Note:
	For any two arbitrary integers m & n, where m > n, a Pythagorean triplet can be
	found by the following formula.
		a = (m*m) - (n*n)
		b = 2 * m * n
		c = (m*m) + (n*n)
"""

def euler():
	m_o = 4
	n_o = 3
	m = 4
	n = 3
	
	while True:
		a = (m*m) - (n*n)
		b = 2 * m * n
		c = (m*m) + (n*n)
		print a + b + c
		
		if( a + b + c >= 1000 ):
			if( a + b + c > 1000 ):
				m_o = m_o + 1
				m = m_o
				n = n_o
				
			if( a + b + c == 1000 ):
				print '-------------'
				print a, b, c
				print a + b + c
				break
		
		n = n + 1
		m = m + 1
	

if __name__ == '__main__':
    euler()