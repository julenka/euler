
from operator import *
import math
import sys
import numpy as np

def printline(str):
    ''' print progress line to stdout

    :param str:
    :return:
    '''
    # \r is carriage return: take us back to the start.
    sys.stdout.write('\r')
    sys.stdout.write(str)
    sys.stdout.flush()


def divisors(n):
    """Finds all of the divisors for a given number, including 1 and itself.

    Returns a list containing all the divisors for a number"""
    ans = []
    for i in range(1, int(math.floor(math.sqrt(n))) + 1):
        if (n % i == 0):
            ans.append(i)
            if (i * i != n):
                ans.append(n / i)
    return ans
	
def isprime(n):
    return len(divisors(n)) == 2

def waysToSum(goal, coins_to_use, index):
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
            ways += waysToSum(dif, coins_to_use, i)
    return ways

def getDigits(number, reverse=False):
    result = []
    while number > 0:
        result.append(number % 10)
        number = number / 10
    if(not reverse):
        result.reverse()
    return result

def generatePermutationsHelper(values):
    result = []
    if len(values) == 1:
        return [values]
    for v in values:
        values_cp = list(values)
        values_cp.remove(v)
        perms = generatePermutationsHelper(values_cp)
        for perm in perms:
            perm.append(v)
        result.extend(perms)
    return result
    
def generatePermutations(n):
    """generates all permutations of the sequence of numbers
    from 1 to n
    """
    return generatePermutationsHelper(range(1,n + 1))

def factorial(x):
    return reduce(mul, range(1, x+1), 1)

def digitsToNum(lst):
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

def toBase(val, base):
    """ Converst val to base base, returns a string
    representation of the result"""
    lst = []
    while (val > 0):
        lst.append(val % base)
        val /= base
    #important to reverse here
    lst.reverse()
    return "".join([str(x) for x in lst])

def isPalindrome(val):
    """ Returns whether val is a palindrome"""
    l1 = list(val)
    l2 = list(val)
    l2.reverse()
    return l1 == l2

def isPandigital(str_val):
    lst = list(str_val)
    lst.sort()
    return lst == [str(i) for i in range(1,len(str_val) + 1)]

def is0Pandigital(str_val):
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

def triangleNumber(n):
    return n * (n+1) / 2.0

def pentagonalNumber(n):
    return n * (3*n - 1) / 2.0

def hexagonalNumber(n):
    return n * (2 * n - 1)

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
