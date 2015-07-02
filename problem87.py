#!/usr/bin/env python

""" Prime power triples
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
"""
__author__ = 'julenka'

from primes import primesfrom2to
# 4th root of 50,000,000 is 84


primes = primesfrom2to(8000)
print primes
count = 0

max_value = 50000000
numbers = set()
for first in primes:
    for second in primes:
        for third in primes:
            sum_primes = first ** 2 + second ** 3 + third ** 4
            if sum_primes < max_value:
                numbers.add(sum_primes)

print len(numbers)