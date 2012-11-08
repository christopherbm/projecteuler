"""rewrite for speed"""
def testing():
	r = range(1, 1000)
	res_three = []
	for i in r:
		m = i % 3
		if(m == 0):
			res_three.append(i)
	
	#print res_three
	
	res_five = []
	for j in r:
		n = j % 5
		if(n == 0):
			res_five.append(j)
	
	#print res_five
	
	all = set(res_three + res_five)
	
	#print all
	
	total = 0
	for a in all:
		total = total + a
		
	print total


if __name__ == '__main__':
    testing()
    print sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
    #print returnModuloOfThree(10)