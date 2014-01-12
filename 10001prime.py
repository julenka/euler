import math

def primesUpTo(max):
	sift = 2
	lst = range(2, max)
	while sift <= math.sqrt(max):
		lst = [x for x in lst if x % lst[0] != 0]
	return lst

print doSift( range(2, 2000))
#print reduce(lambda x, y: x+y, doSift( range(2, MAX_NUMBER)), 0)
