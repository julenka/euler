#!/usr/bin/env python
__author__ = 'julenka'
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

lines = open("data.txt").readlines()
data = []
for l in lines:
    data.append([int(x) for x in l.split()])
max_sums = []
max_sums.append(data[0])

for j,row in enumerate(data[1:]):
    new_row = []
    max_row = max_sums[j]
    for i,v in enumerate(row):
        if i == 0:
            new_v = v + max_row[0]
        elif i == len(row) - 1:
            new_v = v + max_row[-1]
        else:
            new_v = max(v + max_row[i], v + max_row[i - 1])
        new_row.append(new_v)

    max_sums.append(new_row)

print max_sums[-1], max(max_sums[-1])





