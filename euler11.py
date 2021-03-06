"""Question: 
In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26  63  78  14 = 1788696.

What is the greatest product of four adjacent numbers in any direction 
(up, down, left, right, or diagonally) in the 20x20 grid?
"""

def euler():
	r1 = [8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8]
	r2 = [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0]
	r3 = [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65]
	r4 = [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91]
	r5 = [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80]
	r6 = [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50]
	r7 = [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70]
	r8 = [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21]
	r9 = [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72]
	r10 = [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95]
	r11 = [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92]
	r12 = [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57]
	r13 = [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58]
	r14 = [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40]
	r15 = [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66]
	r16 = [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69]
	r17 = [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36]
	r18 = [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16]
	r19 = [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54]
	r20 = [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]
	
	matrix = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]	
	
	high = 0
	
	# run all vertical calculations
	p = calcVertical(matrix)
	if( p > high ): high = p
	
	#run all horizontal calculations
	p = calcHorizontal(matrix)
	if( p > high ): high = p
	
	#run top-left to bottom-right calculations
	p = calcTopLeftToBottomRight(matrix)
	if( p > high ): high = p
	
	#run top-left to bottom-right calculations
	p = calcRightToBottomLeft(matrix)
	if( p > high ): high = p
	
	print high
	
def calcVertical(m):
	high = 0
	for r in m:
		p = productByFour(r)
		if( p > high ): high = p
	
	return high


def calcHorizontal(m):
	high = 0
	
	# create list of horizontal values
	i = 0
	while( i < 20 ):
		m_l = []
		for r in m:
			m_l.append( r[i] )
		
		# calculations on m_l
		p = productByFour(m_l)
		if( p > high ): high = p
		
		i = i + 1		

	return high
	

def calcTopLeftToBottomRight(m):
	""" 
	"""
	high = 0
	
	# length of y
	ly = len(m)
	
	# length of x
	lx = len( m[0] )
	
	y = 0
	x = 0
	while( x < lx ):
		if( x + 3 == lx ):
			# out of bounds, increment y set x to 0
			y = y + 1
			x = 0
			continue
		elif( y + 3 == ly ):
			# out of bounds, end of loop
			break
			
		p0 = m[y][x]
		p1 = m[ y + 1 ][ x + 1 ]
		p2 = m[ y + 2 ][ x + 2 ]
		p3 = m[ y + 3 ][ x + 3 ]
		p  = p0 * p1 * p2 * p3
		
		if( p > high ): high = p
		
		#print p0, p1, p2, p3
		
		# increment x
		x = x + 1
	
	return high


def calcRightToBottomLeft(m):
	""" 
	"""
	high = 0
	
	# length of y
	ly = len(m)
	
	# length of x
	lx = len( m[0] )
	
	y = 0
	x = 0
	while( x < lx ):
		if( x - 3 < 0 ):
			# out of bounds, increment x
			x = x + 1
			continue
		if( y + 3 == ly ):
			break
			
		p0 = m[y][x]
		p1 = m[ y + 1 ][ x - 1 ]
		p2 = m[ y + 2 ][ x - 2 ]
		p3 = m[ y + 3 ][ x - 3 ]
		p  = p0 * p1 * p2 * p3
		
		if( p > high ): high = p
		
		#print p0, p1, p2, p3
		
		# increment
		if( x + 1 == lx ):
			y = y + 1
			x = 1
		else:
			x = x + 1
	
	return high


def productByFour(l):
	high = 0
	i = 0
	n = 4
	while( i < len(l) ):
		s = l[i:i+n]
		
		# validate s
		i = i + 1
		if( len(s) != 4 ): continue
		if( 0 in s ): continue
		if( 1 in s ): continue
		
		p = 1
		for j in s:
			p = p * j
			
		if( p > high ): high = p
	
	return high
	
	
def test():
	r0 = [2, 3, 5, 6]
	r1 = [1, 9, 4, 6]
	r2 = [3, 5, 1, 7]
	r3 = [8, 4, 2, 7]
	m  = [r0, r1, r2, r3]
	
	# length of y
	ly = len(m)
	
	# length of x
	lx = len( m[0] )
	
	print 'length of y and length of x: ', ly, lx
	
	# create vertical rows
	y = 0
	x = 0
	while( x < lx ):
		y = 0
		r = []
		while( y < ly ):
			#r.append([y, x])
			r.append( m[y][x] )
			y = y + 1
			
		print r
		x = x + 1
		
	# create top-down, left-right pairs
	y = 0
	x = 0
	while( x < lx ):
		if( x + 1 == lx ):
			# out of bounds, increment y set x to 0
			y = y + 1
			x = 0
			continue
		elif( y + 1 == ly ):
			# out of bounds, end of loop
			break
			
		#p1 = m[y][x]
		#p2 = m[ y + 1 ][ x + 1 ]
		#p  = p1 * p2
		
		print m[y][x], m[ y + 1 ][ x + 1 ]
		
		# increment x
		x = x + 1
		
	# create top-down right-left pairs
	y = 0
	x = 0
	while( x < lx ):
		if( x - 1 < 0 ):
			# out of bounds, increment x
			x = x + 1
			continue
		if( y + 1 == ly ):
			break
			
		print m[y][x], m[ y + 1 ][ x - 1 ]
		
		# increment
		if( x + 1 == lx ):
			y = y + 1
			x = 1
		else:
			x = x + 1
			
		
if __name__ == '__main__':
	#test()
	euler()