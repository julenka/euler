MAX_NUMBER = 1000000

def doSift(left, lst):
	while left != 0:
		lst = [x for x in lst if x % lst[0] != 0]
		left = left - 1
	return lst[0]

print doSift(1, range(2, MAX_NUMBER))