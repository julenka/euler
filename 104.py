#!/usr/bin/env python
# coding=utf-8
""" Pandigital fibonacci ends

 The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9
pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the
first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital,
find k.
"""
__author__ = 'julenka'

from utils import euler
import math

def fibonacci():
    """ Generates fibonacci numbers

    :return:
    """
    f_n_1 = 1
    f_n_2 = 1
    yield f_n_2
    yield f_n_1
    while 1:
        f_n = f_n_1 + f_n_2
        yield f_n
        f_n_2 = f_n_1
        f_n_1 = f_n

def solve():
    for i, n in enumerate(fibonacci()):
        idx = i + 1
        if idx == 541:
            assert euler.is_pandigital(n % (10 ** 9)), n
        if idx > 541:
            num_zeros = int(math.log10(n))
            first_9 = n / (10 ** (num_zeros - 8))
            last_9 = n % (10 ** 9)
            if euler.is_pandigital(first_9):
                print idx
                if euler.is_pandigital(last_9):
                    return idx


if __name__ == '__main__':
    answer = solve()
    print answer
