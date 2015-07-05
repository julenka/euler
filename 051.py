#!/usr/bin/env python
__author__ = 'julenka'

'''By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.'''

import utils.euler
from collections import Counter, defaultdict
from itertools import combinations
# must be at least 8 primes in the range
# primes must have N of same digit
# same digits must be unique, number 1 to 10
print "getting primes..."
primes = euler_utils.primesUpTo(10**6)
prime_strs = [str(x) for x in primes]

print "generating families..."
# stores a mapping from 53**6 to list of possible completions that are primes. For example,
# *3: [1,2,4,5,7,8]
prime_family = defaultdict(list)

for prime_str in prime_strs:
    counter = Counter(prime_str)
    for star_char, v in counter.iteritems():
        # need to generate all combinations of ***c or *c*
        # for *** we have:
        # **c *c* c**
        # for * we have *cc c*c cc*
        for num_stars in range(v + 1):
            star_indices_gen = combinations(range(v), num_stars)
            for star_indices in star_indices_gen:
                base_array = [star_char] * v
                for idx in star_indices:
                    base_array[idx] = '*'
                s = ""
                base_array_idx = 0
                for c in prime_str:
                    if c == star_char:
                        s += base_array[base_array_idx]
                        base_array_idx += 1
                    else:
                        s += c
                prime_family[s].append(star_char)


family_candidates = {k:v for k,v in prime_family.iteritems() if len(v) >=8}
print family_candidates
