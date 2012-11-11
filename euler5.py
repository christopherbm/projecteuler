"""Question: 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.
What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

def euler():
	i = 2
	r = range(1, 20)
	while(i != 0):
		isAnswer = True
		for j in r:
			if i % j != 0: 
				isAnswer = False
		
		if(isAnswer == True):
			print i
			i = 0
		else:
			i = i + 1
		

if __name__ == '__main__':
    euler()