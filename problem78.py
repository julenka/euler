#!/usr/bin/env python
""" Project Euler problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

"""
__author__ = 'julenka'
import numpy as np

MAX_VALUE = 10000
table = np.zeros((MAX_VALUE,MAX_VALUE))

table[1,1] = 1

for i in range(2,MAX_VALUE):
    table[i, i] = 1
    for smallest_term in range(1, i):
        table[i, smallest_term] = sum(table[i - smallest_term,smallest_term:i])
    num_partitions = sum(table[i,:])
    if num_partitions % 1000000 == 0:
        print i, num_partitions
        exit(1)
    else:
        print i
