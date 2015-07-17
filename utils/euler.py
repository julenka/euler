
from operator import *
import sys
import numpy as np
import itertools

from primes import prime_factorization


def printline(str):
    """ print progress line to stdout

    :param str:
    :return:
    """
    # \r is carriage return: take us back to the start.
    sys.stdout.write('\r')
    sys.stdout.write(str)
    sys.stdout.flush()


def divisors(n):
    """Finds all of the divisors for a given number, including 1 and itself.

    Returns a list containing all the divisors for a number"""
    if n == 1:
        yield 1
        return
    factors = list(prime_factorization(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda a, b: a*b, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def is_prime(n):
    return len(list(divisors(n))) == 2

def ways_to_sum(goal, coins_to_use, index):
    """This function counts the number of ways that you can
    make the goal sum using the available coins. Coins to use
    is a list of possible coins you can use
    """

    if goal == 0:
        return 1
    ways = 0
    for i in range(index, -1, -1):
        coin = coins_to_use[i]
        dif = goal - coin
        if dif >= 0:
            ways += ways_to_sum(dif, coins_to_use, i)
    return ways

def get_digits(number, reverse=False):
    result = []
    while number > 0:
        result.append(number % 10)
        number = number / 10
    if(not reverse):
        result.reverse()
    return result

def sum_digits(number) :
    result = 0
    while number > 0:
        result += number % 10
        number /= 10
    return result

def sum_digits_str(number_str):
    return reduce(lambda acc, new: acc + int(new),number_str, 0)


def generate_permutations(n):
    """generates all permutations of the sequence of numbers
    from 1 to n
    """
    return list(itertools.permutations(range(1, n + 1)))

def factorial(x):
    return reduce(mul, range(1, x+1), 1)

def digits_to_num(lst):
    result = 0
    tens = 0
    for i in range(len(lst)):
        d = lst[i]
        result += d * pow(10, tens)
        tens += 1
    return result

def rotate(lst, n):
    return lst[n:] + lst[:n]

def rotations(lst):
    result = []
    for i in range(len(lst)):
        result.append(rotate(lst, i))
    return result

def to_base(val, base):
    """ Converst val to base base, returns a string
    representation of the result"""
    lst = []
    while (val > 0):
        lst.append(val % base)
        val /= base
    #important to reverse here
    lst.reverse()
    return "".join([str(x) for x in lst])

def is_palindrome(val):
    """ Returns whether val is a palindrome"""
    l1 = list(val)
    l2 = list(val)
    l2.reverse()
    return l1 == l2

def is_pandigital(value):
    digits = set()
    for i in range(1,10):
        digit = value % 10
        if digit == 0:
            return False
        digits.add(digit)
        value = value / 10
        if len(digits) < i:
            return False
    return True

def is_0_pandigital(str_val):
    lst = list(str_val)
    lst.sort()
    return lst == [str(i) for i in range(0,len(str_val) + 1)]

def allPerm(lst):
    """
    Returns a list of lists representing all permutations of items in the input list
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [[lst[0]]]
    result = []
    for i in range(0, len(lst)):
        item = lst[i]
        toAppend = allPerm(lst[0:i] + lst[i+1:])
        for a in toAppend:
            a.insert(0,item)
        result = result + toAppend

    return result;

def triangle_number(n):
    return n * (n+1) / 2.0

def pentagonal_number(n):
    return n * (3*n - 1) / 2.0

def hexagonal_number(n):
    return n * (2 * n - 1)

def choose(n, r):
    """
    n choose r
    """
    return factorial(n) / (factorial(n - r) * factorial(r))


def partitions(n):
    """ Compute number of ways a set of n coins can uniquely be partitioned into groups

    :param n:
    :return:
    """
    # we use a dynamic programing approach:
    # row is # of ways to sum to x, column is maximum value of terms in sum
    # table[waystosumX][with smallestterm]
    table = np.zeros((n+1,n+1))
    table[1,1] = 1

    for i in range(2,n+1):
        table[i, i] = 1
        for smallest_term in range(1, i):
            table[i, smallest_term] = sum(table[i - smallest_term,smallest_term:i])

    return sum(table[n,:])
