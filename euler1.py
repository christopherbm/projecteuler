"""rewrite for speed"""
def testing():
	r = range(1, 1000)
	res = []
	for i in r:
		if( i % 3 == 0 or i % 5 == 0 ):
			res.append(i)
	
	total = sum( set(res) )		
	print total


if __name__ == '__main__':
    testing()
    print sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])