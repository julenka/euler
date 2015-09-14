#!/usr/bin/env python
# coding=utf-8
""" 
"""
__author__ = 'julenka'

def sum_multiples_less_than(n, factor):
    n_multiples = (n - 1) / factor
    one_to_n = n_multiples * (n_multiples + 1) / 2
    return one_to_n * factor

def solve_case(case):
    sum_3 = sum_multiples_less_than(case, 3)
    sum_5 = sum_multiples_less_than(case, 5)
    sum_15 = sum_multiples_less_than(case, 15)
    print sum_3 + sum_5 - sum_15

n_cases = int(input())

for _ in range(n_cases):
    solve_case(int(input()))