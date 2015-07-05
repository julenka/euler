#!/usr/bin/env python
""" Project Euler Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand
lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
__author__ = 'julenka'
import math
values = []
with open("p099_base_exp.txt") as f:
    for idx, line in enumerate(f):
        base, exp = line.split(",")
        base = float(base)
        exp = float(exp)
        values.append((idx + 1, exp * math.log(base)))

print sorted(values, lambda x,y: cmp(y[1], x[1]))[0][0]

