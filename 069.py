# coding=utf-8
__author__ = 'julenka'

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

FORMULA:
φ(n) = n * PRODUCT[unique prime factors p of n] ( 1 - 1/p)
"""

from primes import primesfrom2to
from collections import defaultdict

MAX_VAL = 10 ** 6

# n->set(divisors)
# divisors is set of unique prime factors only
divisor_map = {}

primes = [1] + list(primesfrom2to(MAX_VAL))

# print primes

print "getting unique prime divisors..."
for i in xrange(1, MAX_VAL + 1):
    if i % 10 ** 3 == 0:
        print i
    divisor_map[i] = set()
    j = 1
    while j < len(primes) and primes[j] <= i:
        if i % primes[j] == 0:
            divisor_map[i].add(primes[j])
            other = i / primes[j]
            divisor_map[i] = divisor_map[i].union(divisor_map[other])
            break
        j += 1

# print divisor_map
#
# print "getting relative primes..."
# for i in xrange(1, MAX_VAL + 1):
#     if i % 10 ** 3 == 0:
#         print i
#     for j in xrange(1, i):
#         if relprime(divisor_map[i], divisor_map[j]):
#             relatively_prime[i].append(j)
#
# # print relatively_prime

def phi(n, prime_divisor_set):
    result = float(n)
    for p in prime_divisor_set:
        result *= (1 - 1.0 / float(p))
    return int(result)

phi_n = {k : phi(k,v) for k,v in divisor_map.iteritems()}

max_phi_n = 0
max_n = 0
for n in phi_n:
    n_phi_n = float(n) / phi_n[n]
    if n_phi_n > max_phi_n:
        max_phi_n = n_phi_n
        max_n = n
print max_n, max_phi_n


# import fractions
# MAX_VAL = 10 ** 6
# def phi(n):
#     progress(n)
#     amount = 0
#
#     for k in range(1, n + 1):
#         if fractions.gcd(n, k) == 1:
#             amount += 1
#
#     return amount
#
# def progress(i):
#     if i % 10 ** 3 == 0:
#         print i
#
# def maxRatioGivenMap(mp):
#     max_n = 0
#     max_phi_n = 0
#     for n in mp:
#         n_phi_n = float(n) / mp[n]
#         if n_phi_n > max_phi_n:
#             max_phi_n = n_phi_n
#             max_n = n
#     return (max_n, max_phi_n)
#
#
#
# phi_n = {i: phi(i) for i in xrange(1, MAX_VAL + 1)}
#
# print maxRatioGivenMap(phi_n)
