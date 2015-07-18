#!/usr/bin/env python
# coding=utf-8
""" Largest integer divisible by 2 primes

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3.
For two distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q
and M(p,q,N)=0 if such a positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10 000 000).
"""
__author__ = 'julenka'

from utils import primes

def get_pq(n):
    prime_factors = []
    for prime, exponent in primes.prime_factorization(n):
        if len(prime_factors) > 2:
            return None
        prime_factors.append(prime)
    prime_factors = sorted(prime_factors)
    if len(prime_factors) != 2:
        return None
    return prime_factors[0], prime_factors[1]

def solve():
    result_set = set()
    pq_set = set()
    max_value = 10 ** 7
    for n in range(max_value, 6, -1):
        if n % 10 ** 5 == 0:
            print n
        pq = get_pq(n)

        if pq:
            if pq not in pq_set:
                pq_set.add(pq)
                result_set.add(n)
    return sum(result_set)

if __name__ == '__main__':
    answer = solve()
    print answer
