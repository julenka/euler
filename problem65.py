#/usr/bin/env python
__author__ = 'julenka'
"""
e can be written in form:
2 + 1
    ------
    1 + 1
        ----
        2 + 1
            -----
            1 + 1
                -
                3

[2; 1,2,1,1,4,1,1,6,1,1,8,1,1,...,2k,1]
Find the sum of the digits in numerator of 100th continued fraction of e
"""
from fractions import Fraction

# find 100th term
components =  []
for i in xrange(99):
    if i % 3 != 1:
        components.append(1)
    else:
        components.append( ((i / 3) + 1) * 2)

def findsum(components):
    if len(components) == 0:
        return 0
    head = components[0]
    tail = components[1:]
    return Fraction(numerator = 1, denominator = (head + findsum(tail)) )

def add_digits(n):
    result = 0
    while(n > 9):
        result += (n %  10)
        n /= 10
    result += n
    return result

result = 2 + findsum(components)
print result, add_digits(result.numerator)
