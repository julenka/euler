# coding=utf-8
__author__ = 'julenka'
"""
How many continued fractions for N ≤ 10000 have an odd period?
"""

# b013943 is a number sequence: period of continued fraction for N
f = open("b013943.txt")
oddcount = 0
periods = []
for line in f.readlines():
    i, p = line.split()
    periods.append(int(p))

squares = set([x * x for x in xrange(32)])
irrational_roots = [x for x in xrange(1001) if x not in squares]

print len(irrational_roots)
for p in periods[:len(irrational_roots)]:
    if p % 2 == 1:
        oddcount += 1

print oddcount