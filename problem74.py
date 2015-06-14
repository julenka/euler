#!/usr/bin/env python
# coding=utf-8
""" Project euler problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
__author__ = 'julenka'
import math

def factorial_of_digits(n):
    if n == 0:
        return 1
    digits = []
    while n > 0:
        digits.append(n % 10)
        n /= 10
    return sum((math.factorial(n) for n in digits))

def compute_chain_length(n, terminators):
    initial = n
    result = 0
    values = []
    while n not in terminators:
        values.append(n)
        n = factorial_of_digits(n)

        result += 1
    print "compute_chain_length({}) = {}; {}".format(initial, result, values)
    return result

terminators = {145: 0,
               169: 2,
               363601: 2,
               1454: 2, }[145, 169, 871, 872, 1454, 45361, 45362]

compute_chain_length(69, terminators)
#
# for t in terminators:
#     result = str(t)
#     t_next = factorial_of_digits(t)
#     while t_next != t:
#         result += " -> " + str(t_next)
#         t_next = factorial_of_digits(t_next)
#     result += " -> " + str(t)
#     print result