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
import sys
from collections import Counter

from utils.euler import  printline

def factorial_of_digits(n):
    if n == 0:
        return 1
    digits = []
    while n > 0:
        digits.append(n % 10)
        n /= 10
    return sum((math.factorial(n) for n in digits))

def compute_chain_length(n, terminators):
    values = set()
    while n not in terminators and n not in values:
        values.add(n)
        n = factorial_of_digits(n)

    if n in terminators:
        values |= terminators[n]

    return values

if __name__ == '__main__':
    # example script call: ./problem74.py 1000000
    terminators = {}
    search_below = int(sys.argv[1])
    chain_length_count = Counter()
    for i in range(1, search_below):
        if search_below > 100000:
            printline("{}/{}".format(i, search_below))
        chain = compute_chain_length(i, terminators)
        terminators[i] = chain
        chain_length_count[len(chain)] += 1


    print
    print "maximum chain length: ", max(chain_length_count)
    print "how many of maximum length: ", chain_length_count[60]
