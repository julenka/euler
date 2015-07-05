#!/usr/bin/env python
# coding=utf-8
""" Counting Rectangles



Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""
__author__ = 'julenka'
from scipy.misc import comb

# http://www.gottfriedville.net/mathprob/comb-subrect.html
#
# Another way to reach the answer more quickly is:
#
# In a rectangle m × n there are (m+1) vertical grid lines
# and (n+1) horizontal grid lines (7 and 5 in the example here).
#
# To define any rectangle within the grid,
# we must choose 2 of each and there are
# ( (m+1) choose 2 ) × ( (n+1) choose 2 ) ways to do that.
#
# For 4 × 6 that gives us
# (5 choose 2) × (7 choose 2) =
# 10 * 21 = 210.

def rectangles_m_by_n(m, n):
    return comb(m + 1, 2) * comb( n + 1, 2)

area_rectangles = []
for rows in range(1, 10000):
    for cols in range(1, 10000):
        rectangles = rectangles_m_by_n(rows, cols)
        if rectangles > 2000003:
            break
        area_rectangles.append((rows * cols, rectangles, (rows, cols)))

print sorted(area_rectangles, lambda x, y: cmp(y[1], x[1]))[:20]

