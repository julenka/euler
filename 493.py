#!/usr/bin/env python
""" Under the rainbow

70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).

"""
__author__ = 'julenka'
from utils import euler

num_colors = 7
balls_per_color = 10
max_pick = 20
num_colors_to_count = {x: 0 for x in xrange(num_colors + 1)}

def rcr(colors_left, balls_left, acc):
    """ Recursively Compute how many ways to pick n colors for n in [0, balls_per_color]

    :param colors_left:
    :param balls_left:
    :param acc:
    :return:
    """
    if balls_left < 0:
        return
    if balls_left == 0:
        assert sum(acc.values()) == max_pick
        num_colors_for_set = len(filter(lambda x: x > 0, acc.values()))
        ways = 1
        for _, count in acc.items():
            ways *= euler.choose(balls_per_color, count)
        num_colors_to_count[num_colors_for_set] += ways
        return
    if colors_left <= 0:
        return

    for n in xrange(balls_per_color + 1):
        color_idx = num_colors - colors_left
        acc[color_idx] = n
        rcr(colors_left - 1, balls_left - n, acc)
        acc[color_idx] = 0

rcr(num_colors, max_pick, {}, 0)

s2 = reduce(lambda y, x: x[0] * x[1] + y, num_colors_to_count.items(), 0)

print float(s2) / euler.choose(70, 20)
