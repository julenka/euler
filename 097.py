#!/usr/bin/env python
__author__ = 'julenka'

"""
Find the last 10 digits of 28433 x 2^7830457 + 1
"""


exp=7830457
result = 1


for i in xrange(exp):
    result *=2
    result %= 10**10

print (result * 28433 + 1) % 10 ** 10
