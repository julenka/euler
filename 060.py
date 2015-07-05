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
from math import factorial
import sys

MAX_PRIME = 10 ** 9
N = 4
print "finding primes..."
primes = set(primesfrom2to(MAX_PRIME))
candidates = primesfrom2to(10 ** 5)
def test(a):
    for p1, p2 in itertools.permutations(a, 2):
        s1, s2 = str(p1), str(p2)
        if int(s1 + s2) not in primes:
            return False
    return True

def choose(n, r):
    """
    n choose r
    """
    return factorial(n) / (factorial(n - r) * factorial(r))

def printline(s):
    sys.stdout.write("{} \r".format(s) )
    sys.stdout.flush()


print "doing test..."
pairs = defaultdict(set)
n_candidates = len(candidates)
n_combinations = choose(n_candidates, 2)
for i, (p1, p2) in enumerate(itertools.combinations(candidates, 2)):
    printline("{}/{}".format(i, n_combinations))
    if test([p1, p2]):
        pairs[p1].add(p2)
        pairs[p2].add(p1)

print "finding sets..."


for p1, v1 in pairs.iteritems():
    for p2 in v1:
        s = pairs[p1] & pairs[p2]
        if len(s) > 0:
            for p3 in s:
                s2 = s & pairs[p3]
                if len(s2) > 0:
                    for p4 in s2:
                        s3 = s2 & pairs[p4]
                        if len(s3) > 0:
                            for p5 in s3:
                                print p1, p2, p3, p4, p5, "sum:", sum([p1, p2, p3, p4, p5])
                                exit(0)