#!/usr/bin/env python
# coding=utf-8
""" Project Euler problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

10 9
100 74
1000 449
10000 599
100000 949
1000000
"""
__author__ = 'julenka'

import sys

try:
    MAX_VALUE = int(sys.argv[1])
    MOD_VALUE = int(sys.argv[2])
except IndexError:
    print "usage: problem78.py MAX_VALUE MOD_VALUE"

# P(n) = Σ (-1)k+1[P(n - k(3k-1)/2) + P(n - k(3k+1)/2)],
#
# where k ranges from 1 to n. Because P(b) = 0 for all negative integers b, many of the terms in this series vanish. As an example, let's use the above formula to compute P(13) and P(15).
#
# P(13) = P(13-1) + P(13-2) - P(13-5) - P(13-7) + P(13-12) + P(13-15) - ...
# = P(12) + P(11) - P(8) - P(6) + P(1) + P(-2) - ...
# = 77 + 56 - 22 - 11 + 1 + 0 - ....
# = 101.
#
# P(15) = P(15-1) + P(15-2) - P(15-5) - P(15-7) + P(15-12) + P(15-15) - ...
# = P(14) + P(13) - P(10) - P(8) + P(3) + P(0) - ...
# = 135 + 101 - 42 - 22 + 3 + 1 - ....
# = 176.

p = []
p.append(1)
for n in range(1, MAX_VALUE):
    result = 0
    # print "P({}) = ".format(n)
    for k in range(1, n + 1):
        multiplier = (-1) ** (k + 1)
        x_1 = n - k * (3 * k - 1) / 2
        y_1 = 0
        if x_1 >= 0:
            y_1 = p[x_1]
        x_2 = n - k * (3 * k + 1) / 2
        y_2 = 0
        if x_2 >= 0:
            y_2 = p[x_2]
        # print "\t{} * (P({}) + P({})) + ".format(multiplier, x_1, x_2)
        result += multiplier * (y_1 + y_2)
    p.append(result)
    if(n % 1000 == 0):
        print n
    if result % MOD_VALUE == 0:
        print n, result
        exit(0)
