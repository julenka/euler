acc = 0
for x in range(1000):
	if x % 3 == 0:
		acc += x
	elif x % 5 == 0:
		acc += x

print acc