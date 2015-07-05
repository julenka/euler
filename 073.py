#!/usr/bin/env python
# coding=utf-8
""" Project Euler problem 73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

"""
__author__ = 'julenka'

from fractions import gcd

max_d = 12000

result = 0
for d in range(2, max_d + 1):
    print d
    for n in range(1, d):
        if d / 3.0 < n < d / 2.0:
            if gcd(n, d) == 1:
                result += 1

print result
