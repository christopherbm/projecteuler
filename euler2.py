def euler():
	
	f = [1,2]
	i = 0
	j = 1
	while f[j] < 4000000:
		f.append( f[i] + f[j] )
		i = i + 1
		j = j + 1
	
	print f
	total = 0
	for n in f:
		if n % 2 == 0:
			print n
			total = total + n
			
	print total

if __name__ == '__main__':
    euler()