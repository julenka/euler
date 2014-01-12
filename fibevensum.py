acc = 0
prev = 1
cur = 1
while cur < 4000000:
	if cur % 2 == 0:
		acc += cur
	next = prev + cur
	prev = cur
	cur = next
	print "cur %i" % cur
	
print "acc: %i" % acc