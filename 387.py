#!/usr/bin/env python
# coding=utf-8
""" Harshad numbers

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a
right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""
__author__ = 'julenka'

from utils import euler
from collections import deque

def is_harshad(n):
    return n % euler.sum_digits(n) == 0

def is_right_truncatable(n):
    while n > 0:
        if not is_harshad(n):
            return False
        n /= 10
    return True

# is_strong_harshad
def is_strong_harshad(n):
    """ Determine if n / (sum of digits of n) is prime

    :param n:
    :return:
    """
    sum_digits = euler.sum_digits(n)
    return n % sum_digits == 0 and euler.is_prime(n / sum_digits)

def right_truncatable_generator():
    """ Generates right truncatable harshad numbers

    :return:
    """
    to_inspect = deque()
    to_inspect.extend(xrange(1, 10))
    while len(to_inspect) > 0:
        cur_value = to_inspect.popleft()
        if is_harshad(cur_value):
            yield cur_value
            for new_digit in xrange(10):
                to_inspect.append(cur_value * 10 + new_digit)



def solve(max_value):
    strong_right_truncatable_harshad_primes = []
    for right_truncatable in right_truncatable_generator():
        # for each right truncatable number, figure out if it is strong,
        # prime. If so add to sum
        if is_strong_harshad(right_truncatable):
            for new_digit in xrange(10):
                to_test = right_truncatable * 10 + new_digit
                if euler.is_prime(to_test):
                    strong_right_truncatable_harshad_primes.append(to_test)
                if to_test > max_value:
                    return sum(strong_right_truncatable_harshad_primes)
    return sum(strong_right_truncatable_harshad_primes)

if __name__ == '__main__':
    assert is_harshad(201)
    assert is_strong_harshad(201)
    answer = solve(10**14)
    print answer
