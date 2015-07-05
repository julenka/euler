#!/usr/bin/env python
""" Project Euler problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

"""
__author__ = 'julenka'

# I came up with a dynamic programming solution on my own, but this topic is
# related to partition theory:
# Related: https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function

from utils.euler import  partitions
import numpy as np
import sys
goal_value = int(sys.argv[1])


print partitions(goal_value) - 1







