#!/usr/bin/env python
max_sum = 0
for i in xrange(1,100):
	nstr = str(pow(99,i))
	str_sum = sum([int(x) for x in nstr])	
	if str_sum > max_sum:
		max_sum = str_sum

print "max: ", max_sum
