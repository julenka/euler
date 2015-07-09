#!/usr/bin/env python
""" Under the rainbow

70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).

"""
__author__ = 'julenka'
from utils import euler
from collections import Counter

NUM_COLORS = 7
BALLS_PER_COLOR = 10
NUM_BALLS_TO_PICK = 20

def rcr(colors_left, balls_left, color_to_count, num_colors_to_ways):
    """ Recursively Compute how many ways to pick n colors for n in [0, balls_per_color]

    This method modifies num_colors_to_ways.

    :param colors_left: how many colors are left
    :param balls_left: how many balls are left
    :param color_to_count: color_idx -> # balls of that color
    :return: None. Modifies num_colors_to_ways
    """
    if balls_left < 0:
        return
    if balls_left == 0:
        assert sum(color_to_count.values()) == NUM_BALLS_TO_PICK
        num_colors_for_set = len(filter(lambda x: x > 0, color_to_count.values()))
        ways = reduce(lambda accumulator, new_value: euler.choose(BALLS_PER_COLOR, new_value) * accumulator,
                      color_to_count.values(), 1)
        num_colors_to_ways[num_colors_for_set] += ways
        return
    if colors_left <= 0:
        return

    for n in xrange(BALLS_PER_COLOR + 1):
        color_idx = NUM_COLORS - colors_left
        color_to_count[color_idx] = n
        rcr(colors_left - 1, balls_left - n, color_to_count, num_colors_to_ways)
        color_to_count[color_idx] = 0

def solve():
    num_colors_to_ways = Counter()
    rcr(NUM_COLORS, NUM_BALLS_TO_PICK, {}, num_colors_to_ways)

    s2 = reduce(lambda y, x: x[0] * x[1] + y, num_colors_to_ways.items(), 0)
    print float(s2) / euler.choose(70, 20)

if __name__ == '__main__':
    solve()
