#!/usr/bin/env python
__author__ = 'julenka'


"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import itertools
from primes import primesfrom2to
from collections import defaultdict

prime_pow = 10
MAX_PRIME = 10 ** prime_pow
print "finding primes..."
primes = primesfrom2to(MAX_PRIME)
prime_set = set(primes)
initial_primes = [3,7,109,673]

def test(a):
    for p1, p2 in itertools.permutations(a, 2):
        s1, s2 = str(p1), str(p2)
        if int(s1 + s2) not in prime_set:
            return False
    return True

print "doing test..."

for p in primes:
    print p
    if len(str(p)) + 3 > prime_pow:
        print "max exceeded"
        break

    new_set = initial_primes + [p]
    if test(new_set):
        print new_set, sum(new_set)
        break


