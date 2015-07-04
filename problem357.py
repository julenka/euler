#!/usr/bin/env python
""" Prime generating integers

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.

"""
__author__ = 'julenka'

from euler_utils import divisors
from primes import primesfrom2to

max_value = 100000000
primes = set(primesfrom2to(max_value * 2))

valid = []
result = 0
import time
start_time = time.time()
for i in xrange(1, max_value):
    if i % 1000000 == 0:
        end_time = time.time()
        elapsed = end_time - start_time
        start_time = end_time
        print i, elapsed, "seconds"
    divisors_of_i = divisors(i)
    for d in divisors_of_i:
        if not (d + i / d in primes):
            break
    else:
        result += i

print result
