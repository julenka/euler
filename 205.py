"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
__author__ = 'julenka'

# Solutino 2: Try to compute probabilities
import itertools
from collections import Counter

def get_map(sides, count):
    result = Counter()
    for x in itertools.product(range(1,sides + 1), repeat=count):
        result[sum(x)] += 1
    return result


def get_cumsum(mp):
    cumsum = {}
    for k in sorted(mp.keys()):
        cumsum[k] = mp[k]
        if k - 1 in cumsum:
            cumsum[k] += cumsum[k - 1]
    return cumsum

# sume => count
pyramid_map = get_map(4, 9)
pyramid_ways = 4 ** 9
pyramid_cumsum = get_cumsum(pyramid_map)
print pyramid_cumsum

cube_map = get_map(6, 6)
cube_ways = 6 ** 6
cube_cumsum = get_cumsum(cube_map)

# min sum that pyramid has is 9 (9 dice)
total_prob = 0
for i in xrange(9, 37):
    prob_i = pyramid_map[i] / float(pyramid_ways)
    prob_beat_given_i = cube_cumsum[i - 1] / float(cube_ways)
    total_prob += prob_i * prob_beat_given_i
print total_prob

# Solution 1: brute force.
# from random import randint
#
# pete_wins = 0
# rounds = 10**9
#
# for i in xrange(rounds):
#     pete_score = 0
#     colin_score = 0
#     for j in xrange(9):
#         pete_score += randint(1,4)
#     for j in xrange(6):
#         colin_score += randint(1,6)
#     if pete_score > colin_score:
#         pete_wins += 1
#
# print float(pete_wins) / rounds

