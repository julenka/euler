import math

def pFactors(x):
	if x == 1:
		return [1]
	result = []
	sqrt_x =  math.floor(math.sqrt(x))
	for i in range(2, sqrt_x + 1):
		print i
		if x % i == 0:
			result.extend(pFactors(i))
			result.extend(pFactors(x / i))
			return result
	return [x]

print pFactors(600851475143)