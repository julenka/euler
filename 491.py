#!/usr/bin/env python
# coding=utf-8
""" Double pandigital numbers

 We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero).
 For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?
"""
__author__ = 'julenka'

# quick rule to check if divisible by 11: get alternating sum of digits from left to right
# and check if that is divisible by 11
# for example 2728 = 2 - 7 + 2 - 8 = -11 which is divisible by 11

from itertools import permutations
from collections import Counter
import math

def helper(digits):
    num_digits = sum(digits.values())
    if num_digits == 0:
        yield 0
    for element, count in digits.iteritems():
        if count == 0:
            continue
        if sum(digits.values()) == 20 and element == 0:
            continue
        digits[element] -= 1
        for j in helper(digits):
            yield element * (10 ** (num_digits - 1)) + j
        digits[element] += 1

def double_pandigital_generator():
    """ Generates double pandigital numbers as lists
    :return:
    """
    digits = Counter(range(10) * 2)
    for number in helper(digits):
        yield number

def is_divisible_by_11(lst):
    sum_even = sum(lst[::2])
    sum_odd = sum(lst[1::2])
    print sum_even - sum_odd
    return (sum_even - sum_odd) % 11 == 0

def is_divisible_by_11(n):
    return n % 11 == 0

def solve():
    answer = 0
    for i, pandigital_sequence in enumerate(double_pandigital_generator()):
        if is_divisible_by_11(pandigital_sequence):
            print pandigital_sequence
            answer += 1
        if answer > 100:
            break
    return answer

if __name__ == '__main__':
    answer = solve()
    print answer
