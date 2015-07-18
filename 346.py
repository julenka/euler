#!/usr/bin/env python
# coding=utf-8
""" Repunits

 The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit.
It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10**12.
"""
__author__ = 'julenka'

from utils.timer import Timer
import math

def repunit_base(reps, base):
    result = 0
    for exponent in xrange(reps):
        result += base ** exponent
    return result

def test_repunit_base():
    assert repunit_base(1, 2) == 1
    assert repunit_base(1, 1000) == 1
    assert repunit_base(2, 2) == 3
    assert repunit_base(3, 2) == 7
    assert repunit_base(2, 6) == 7

def solve():
    max_value = 10 ** 12
    cache = set([1])
    result = 1
    for base in xrange(2, int(math.sqrt(max_value))):
        reps = 3
        base10 = repunit_base(reps, base)
        while base10 < max_value:
            if base10 not in cache:
                cache.add(base10)
                result += base10
            reps += 1
            base10 = repunit_base(reps, base)
    return result

if __name__ == '__main__':
    test_repunit_base()
    with Timer() as t:
        t.verbose = True
        answer = solve()
    print answer
