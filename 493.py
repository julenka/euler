#!/usr/bin/env python
""" Under the rainbow
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
__author__ = 'julenka'

# from utils import euler
# from collections import Counter
#
# sets_of_balls = euler.choose(70, 20)
# print sets_of_balls
#
# def rcr(n_balls, k_colors, max_size, depth):
#     # print "{} rcr({},{},{}):".format("\t" * depth, n_balls, k_colors, max_size)
#     if n_balls == 0 and k_colors == 0:
#         return Counter({0: 1})
#
#     if n_balls == 0 or k_colors == 0:
#         # print "{} rcr({},{},{}) return {}".format("\t" * depth, n_balls, k_colors, max_size, Counter({n_balls: k_colors}))
#         return Counter({n_balls: k_colors})
#
#     if n_balls < 0:
#         raise Exception("unexpected value n_balls {}".format(n_balls))
#
#     ways = rcr(n_balls, k_colors - 1, max_size, depth + 1)
#
#     for balls_for_color in xrange(1, min(n_balls + 1, max_size + 1)):
#         if n_balls - balls_for_color < 0:
#             continue
#         ways2 = rcr(n_balls - balls_for_color, k_colors - 1, max_size, depth + 1)
#         ways3 = Counter()
#         for k, v in ways2.items():
#             ways3[k + 1] = v
#         ways += ways3
#     # print "{} rcr({},{},{}) return {}".format("\t" * depth, n_balls, k_colors, max_size, ways)
#     return ways
#
# total_ways = rcr(20, 7, 10, 0)
# print total_ways
#
# result_sum = reduce(lambda y, x: x[0] * x[1] + y, total_ways.items(), 0)
# print result_sum
#
# print float(result_sum) / sets_of_balls
#
# print float(result_sum) / sum(total_ways.values())

from multiprocessing.pool import Pool
import time
import numpy as np
from collections import Counter

counter = Counter()
def job_worker(args):
    num_iterations, worker_idx = args
    balls = np.array([x / 10 for x in range(70)])

    balls_to_pick = 20

    expected_value_sum = 0
    start_time = time.time()

    for i in xrange(num_iterations):
        np.random.shuffle(balls)
        print balls
        picked_balls = set(balls[:balls_to_pick])
        expected_value_sum += len(picked_balls)
        counter[len(picked_balls)] += 1
        if i % 1000000 == 0:
            elapsed = time.time() - start_time
            print "worker", worker_idx, i, expected_value_sum, "elapsed", elapsed
            start_time = time.time()
    return expected_value_sum


num_workers = 1

iterations_per_worker = 1375400
#
# pool = Pool(processes=num_workers)
# input_array = [iterations_per_worker] * num_workers
# results = pool.map(job_worker, zip(input_array, xrange(num_workers)))
result = job_worker((iterations_per_worker, 1))
print result


print result / (iterations_per_worker * num_workers)

print counter