#!/usr/bin/env python
"""
	Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

	37 36 35 34 33 32 31
	38 17 16 15 14 13 30
	39 18  5  4  3 12 29
	40 19  6  1  2 11 28
	41 20  7  8  9 10 27
	42 21 22 23 24 25 26
	43 44 45 46 47 48 49

	It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting 
	is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

	If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
	If this process is continued, what is the side length of the square spiral for which the ratio of primes along 
	both diagonals first falls below 10%?
"""
__author__ = "Julia Schwarz"

from primes import primesfrom2to


primes = set(primesfrom2to(10**9))

pct = 1.0
level = 1
diagonals = [1]
num_primes = 0
print "level, side_length, n_diagonals, n_primes, pct"
while pct >= 0.1:
	side_length = 2 * level + 1
	square = side_length ** 2
	for i in xrange(4):
		corner = square - (side_length - 1) * i
		diagonals.append(corner)
		if corner in primes:
			num_primes += 1
	pct = float(num_primes) / len(diagonals)
	print level, side_length, len(diagonals), num_primes, pct, max(diagonals)
	level += 1
print max(primes)