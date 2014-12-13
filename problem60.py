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

MAX_PRIME = 10 ** 6
N = 3
print "finding primes..."
primes = primesfrom2to(MAX_PRIME)
def test(a):
    for p1, p2 in itertools.permutations(a, 2):
        s1, s2 = str(p1), str(p2)
        if int(s1 + s2) not in primes:
            return False
    return True

print "doing test..."
pairs = set()
possible = set()
for p1, p2 in itertools.combinations(primes, 2):
    if test([p1, p2]):
        pairs.add((p1, p2))
        pairs.add((p2, p1))
        possible.add(p1)

result = {}
for possible_set in itertools.combinations(possible, N):
    for pair in itertools.permutations(possible_set, 2):
        if pair not in pairs:
            print pair
            break
    else:
        result[sum(possible_set)] = possible_set

print possible
print result


