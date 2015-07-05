#!/usr/bin/env python
__author__ = 'julenka'

"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def digits_in(n):
    return len(str(n))

nth_powers = set()

for i in range(1,10):
    exp = 1
    while exp <= digits_in(i ** exp):
        if digits_in(i ** exp) == exp:
            nth_powers.add(i ** exp)
        exp += 1

print len(nth_powers)