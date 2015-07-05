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
import math

max_value = 100000000
primes = set(primesfrom2to(max_value * 2))

valid = []
result = 0

def test_number(n):
    for i in xrange(1, int(math.sqrt(n)) ):
        if n % i == 0:
            if n / i + i in primes:
                return True
    return False

for i in xrange(1, max_value):
    if test_number(i):
        result += i

print result
