import math

def primesUpTo(max):
	result = []
	lst = range(2, max)
	sift = lst.pop(0)
	result.append(sift)
	while sift <= math.sqrt(max):
		lst = [x for x in lst if x % sift != 0]
		sift = lst.pop(0)
		result.append(sift)

	result.extend(lst)
	return result

print reduce(lambda x, y: x+y, primesUpTo( 2000000), 0)

