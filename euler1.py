"""Question:
Original link: http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

def euler():
	r = range(1, 1001) # 1 is included, 1001 is not included
	res = []
	for i in r:
		if( i % 3 == 0 or i % 5 == 0 ):
			res.append(i)
	
	total = sum( set(res) )	# set function removes duplicate values from list
	print total


if __name__ == '__main__':
    euler()