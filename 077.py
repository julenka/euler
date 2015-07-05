#!/usr/bin/env python
""" Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

"""
__author__ = 'julenka'

from primes import primesfrom2to
import sys
import itertools
if len(sys.argv) < 2:
    print "usage: {} prime_max_value max_primes_in_sum".format(__file__)
    exit(1)
prime_max_value = int(sys.argv[1])
max_primes_in_sum = int(sys.argv[2])
primes = primesfrom2to(prime_max_value)

upper_bound = 83

from collections import Counter
prime_summations_count = Counter()
for combination_length in xrange(1, max_primes_in_sum + 1):
    candidate_primes = [x for x in primes if 2 * combination_length - 2 + x < upper_bound]
    for combinations in itertools.combinations_with_replacement(candidate_primes, combination_length):
        prime_sum = sum(combinations)
        prime_summations_count[prime_sum] += 1

prime_summations_gt_5000 = filter(lambda (x, y): y > 5000, prime_summations_count.items())
print sorted(prime_summations_gt_5000)