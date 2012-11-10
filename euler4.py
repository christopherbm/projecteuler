"""Question: 
A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91*99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def euler():
	largest_palidrome = 0
	n = 1
	while(n <= 99):
		i = 1
		while(i <= 99):
			m = i * n

			# convert number to string and
			# only proceed if number has more than 1 digit
			m = str(m)
			length = len(m) - 1
			if( length > 0 ):
				# reverse m
				m_r = m[::-1]
				
				j = 0
				not_palidrome = False
				while(j <= length):
					if m[j] != m_r[j]:
						not_palidrome = True
					j = j + 1
				
				# double negative logic - change later to be more concise
				if(not_palidrome == False):
					m = int(m)
					if(m > largest_palidrome):
						largest_palidrome = m
					
			# increment internal while loop
			i = i + 1
		
		#increment external while loop
		n = n + 1
		
	print largest_palidrome


if __name__ == '__main__':
    euler()