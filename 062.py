#!/usr/bin/env python
__author__ = 'julenka'
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from collections import defaultdict
MAX = 10 ** 5
cubes = defaultdict(list)
for i in xrange(MAX):
    v = str(i ** 3)

    cubes["".join(sorted(v))].append(i)

cubes = {k:v for k,v in cubes.iteritems() if len(v) == 5 }
all_values = reduce(lambda a,b:a+b,cubes.values(),[])
min_v = min(all_values)
min_v_k ="".join(sorted(str(min_v ** 3)))
print min_v, min_v ** 3, cubes[min_v_k]
