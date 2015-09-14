#!/usr/bin/env python
# coding=utf-8
__author__ = 'julenka'

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

def add_square_digits(n):
    result = 0
    while(n > 9):
        result += (n %  10) ** 2
        n /= 10
    result += n ** 2
    return result

answer = 0
cache = {1:1, 89: 89}
for i in range(1,10 ** 1):
    print i
    cur = i
    chain = [i]
    while cur != 1 and cur != 89 and cur not in cache:
        cur = add_square_digits(cur)
        chain.append(cur)
    if cur == 1 or cur == 89:
        for link in chain:
            cache[link] = cur
    if cache[cur] == 89:
        answer += 1


print answer