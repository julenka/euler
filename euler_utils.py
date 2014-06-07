
from operator import *
import math

dct = dict()
dct[1] = 1
lst = []
maxhops = 0
maxhopsn = 0

def hopsForNumber(n):
    """Unfortunately, I don't remember what this function does
    so this comment is pretty useless :P
    """
    global maxhops
    global maxhopsn
    hops = 0
    if dct.has_key(n):
        return dct[n]
    if n % 2 == 0:
        hops = hopsForNumber(n / 2) + 1
    else:
        hops = hopsForNumber(3 * n + 1) + 1
    dct[n] = hops
    if(hops  > maxhops):
        maxhops = hops
        maxhopsn = n
    return hops

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



def primeSieve(lst):
    i = 0
    while lst[i] <= math.sqrt(lst[-1]):
        sift = lst[i]
        lst = [x for x in lst if (x == sift or x % sift != 0)]
        i = i + 1
    return lst
    
def primesUpTo(m):
    return primeSieve(range(2, m))

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

def nChooseR(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    
    
