#!/usr/bin/python
# This file contains solutions to project euler problems
# each function calculates the solution for a problem
# and returns the answer.
from utils.euler import *
import numpy as np


def p13():
    f = open("euler13.txt", "r")
    acc = []
    next = []
    for line in f:
        next = [int(x) for x in list(line.strip())]
        if not acc:
            acc = next
        else:
            acc = map(sum, zip(acc, next))
            result = []
            carry = 0
            acc.reverse()
        for x in acc:
            x = x + carry
            result.append(x % 10)
            carry = x / 10
            
    result.append(carry)
    result.reverse()
    return result
                
def p16():
    lst = list( 
"10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376");

    vals = [int(x) for x in lst];
    return reduce(lambda x,y: x+y, vals);

def p17():
    b10 = [3,3,5,4,4,3,5,5,4]
    tentwenty = [3,6,6,8,8,7,7,9,9,8]
    #one throgh nineteen
    oneten = sum(b10)
    tenninteen = sum(tentwenty)
    b100 = [6,6,6,5,5,7,7,6]
    #to 99
    twentyninetynine = sum(b100) * 10 + oneten * 8
    one99 = oneten + tenninteen + twentyninetynine
    #100 to 999
    hundred999 = 900 * 7 + oneten * 100 + 3 * 891 + one99 * 9
    return hundred999 + 3 + 8

def p25():
    first = 1
    second = 1
    term =2
    while (len(list(str(second))) < 1000):
        tmp = second
        second = second + first
        first = tmp
        term = term + 1
    return term

def p26():
    cycles = []
    for val in range (2, 1000):
        remainders = []
        goal = 10
        r = goal % val
        while(r != 0 and not r in remainders):
            remainders.append(r)
            goal = r * 10
            r = goal % val
        if(r == 0):
            cycles.append(0)
        else:
            cycles.append(len(remainders) - remainders.index(r))
    ans = max(cycles)
    return cycles.index(ans) + 2

def p27():
    maxlen = 0
    maxprod = 0
    primes = set()
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            seq = []
            n = 0
            rslt = n * n + a * n + b
            while rslt > 0 and (rslt in primes or is_prime(rslt)):
                seq.append(rslt)
                if not rslt in primes:
                    primes.add(rslt)
                n = n + 1
                rslt = n * n + a * n + b
            if (len(seq) > maxlen):
                print(f"a: {a} b: {b} seq: {seq}")
                maxlen = len(seq)
                maxprod = a * b

    return maxprod

def p28():
    answer = 1
    curval = 1
    for i in range(3, 1002, 2):
        print(i)
        for j in range(0, 4):
            curval = curval + i - 1
            answer = answer + curval
    return answer

def p29():
    s = set()
    for i in range(2, 101):
        for j in range(2, 101):
            s.add(pow(i,j))
    return len(s)

def p30():
    ans = 0
    for i in range(10, 1000000):
        s = 0
        save = i
        while i > 0:
            digit= i % 10
            s = s + pow(digit, 5)
            i = i / 10
        if s == save:
            print(s)
            ans = ans + s
    return ans

def p31():
    pence = [1,2,5,10,20,50,100,200]
    return ways_to_sum(200, pence, len(pence) - 1)

def p32():
    perms = generate_permutations(9)
    results = set()
    for p in perms:
        first = p[0] * 10 + p[1]
        second = 100 * p[2] + 10 * p[3] + p[4]
        product = 1000 * p[5] + 100 * p[6] + 10 * p[7] + p[8]
        if first * second == product:
            results.add(product)
        first = p[0]
        second = 1000 * p[1] + 100 * p[2] + 10 * p[3] + p[4]
        product = 1000 * p[5] + 100 * p[6] + 10 * p[7] + p[8]
        if first * second == product:
            results.add(product)

    print(results)
    answer = 0
    for r in results:
        answer += r
    return answer

def p33():
    """The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """
    nontrivial = list()
    for num in range(11, 100):
        numF = float(num)
        numDs = zip(get_digits(num), get_digits(num, True))
        
        for denom in range(num + 1, 100):

            denomF = float(denom)
            denomDs = zip(get_digits(denom), get_digits(denom, True))
            
            goal = numF/denomF

            for (cancel, keep) in numDs:
                for (cancel2, keep2) in denomDs:
                    if cancel == cancel2 and cancel != 0 and keep != 0 and keep2 != 0:
                        nF = float(keep)
                        dF = float(keep2)

                        
                        if nF / dF == goal:
                            nontrivial.append((num, denom))
            
    numAns = 1
    denomAns = 1

    for (x,y) in nontrivial:
        numAns *= x
        denomAns *= y

    return (numAns, denomAns)
                
def p34():
    """145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """

    result = []
    for i in range (1, 100000):
        d = get_digits(i)
        digits = [factorial(x) for x in d]
        s = sum(digits)
        if s == i and len(digits) > 1: 
            result.append(s)
    print(result)
    return sum(result)

def p35():
    """
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    
    How many circular primes are there below one million?
    """
    primes = set([x for x in range(1, 1000000) if is_prime(x)])
    print(primes)
    ans = []
    for i in range(1, 1000000):
        r = [digits_to_num(x) for x in rotations(get_digits(i))]
        prime = True
        rprime = [x for x in r if x in primes]
        if len(rprime) == len(r):
            ans.append(i)
    return ans

def p36():
    """ 
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """
    palindromes = []
    for i in range(1, 1000000):
        base10 = to_base(i, 10)
        if (is_palindrome(base10)):
            base2 = to_base(i, 2)
            if(is_palindrome(base2)):
                palindromes.append(int(base10))

    return sum(palindromes)

def p37():
    """
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    2,3,5,7 are not truncatable
    """
    primes = set([2,3,5,7])
    truncatable_primes = []
    current = 11
    while len(truncatable_primes) < 11:
        if(is_prime(current)):
            primes.add(current)
            curStr = str(current)
            # truncate from both left and right and see if prime at each step
            right = [curStr[:i] for i in range(1, len(curStr))]
            valid = True
            for r in right:
                if not int(r) in primes:
                    valid = False
                    break
            # If valid, check from the left
            if valid:
                left = [curStr[i:] for i in range(1, len(curStr))]
                for l in left:
                    if not int(l) in primes:
                        valid = False
                        break
            
            if valid:
                truncatable_primes.append(current)
                print(f"truncatable: {current} len: {len(truncatable_primes)}")
        # increment by 2 since even numbers are never prime    
        current += 2
    return truncatable_primes

def p38():
    """Take the number 192 and multiply it by each of 1, 2, and 3:

    192  1 = 192
    192  2 = 384
    192  3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n  1?"""

    # start from the highest number, 9876, and go down, seeing if it can form
    panDigitals = []
    p38Helper("9", list("12345678"), panDigitals)
    panDigitals.sort(reverse = True)
    return panDigitals

def p38Helper(base, remaining, acc):
    if len(base) == 4:
        if canFormPanDigital(int(base)):
            acc.append(base)
        return
    if canFormPanDigital(int(base)):
        acc.append(base)
    for r in remaining:
        remaining2 = list(remaining)
        remaining2.remove(r)
        p38Helper(base + r, remaining2, acc)
    
def canFormPanDigital(val):
    result = ""
    oneto9=list("123456789")
    for i in range(1,10):
        result += str(val * i)
        if len(result) == 9:
            resultL = list(result)
            resultL.sort()
            return resultL == oneto9
        elif len(result) > 9:
            return False

def p39():
    """
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}
    
    For which value of p  1000, is the number of solutions maximised?
    """
    perimCounts = dict()
    # Need to look at sides max length 333
    for i in range(1, 500):
        for j in range(1, 500):
            k = (i * i + j * j) ** .5
            if int(k) == k:
                # sum perimeter
                perim = i + j + k
                if perim <= 1000:
                    if not perimCounts.has_key(perim):
                        perimCounts[perim] = 0
                    perimCounts[perim] += 1
    print(perimCounts[120])
    maxPerimValue = 0
    maxPerim = 0
    for (k,v) in perimCounts.items():
        if v > maxPerimValue:
            maxPerimValue = v
            maxPerim = k
    return (maxPerim, maxPerimValue)

def p40():
    """
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1  d10  d100  d1000  d10000  d100000  d1000000
    """
    s = "".join([str(x) for x in range(1,200000)])
    return int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

def p41():
    """
    Find the largest n-digit pandigital prime that exists?
    """
    for i in range(2,8):
        print(f"looking at pandigital values of length {i}")
        maxv = int("".join([str(j) for j in range(i,0,-1)]))
        print("getting primes...")
        primes = primesUpTo(maxv)
        primes = [x for x in primes if len(str(x)) == i]
        primes.reverse()

        for p in primes:
            if is_pandigital(str(p)):
                print(p)

def p42():
    """
    Find the number of triangle words in words.txt
    """
    # read each line of words and convert it to a number
    f = open('words.txt','r')
    words = [s.strip("\"").lower() for s in f.readline().split(",")]
    # convert each word to a number
    numbers = [sum([ord(s) - ord("a") + 1 for s in word]) for word in words]
    # check which of these numbers is a triangle by seeing is n^2 + n - (result * 2) = 0
    # check if -1 - (1 - ( - 8n)) is divisible by 2

    total = 0
    for i in numbers:
        numerator = -1 - math.sqrt(1 + 8 * i)
        if numerator % 2 == 0:
            total+=1
            print(i)
    print(f"total: {total}")
    
    

def p43helper(divisibleBy):
    # find all 3 digit numbers divisible by divisibleBy
    d17 = [x for x in range(0,1000) if x % divisibleBy == 0]
    # filter out the numbers so only ones with unique numbers stay
    d17 = [x for x in d17 if (x/100 != x/10 % 10 and x / 100 != x % 10 and x / 10 % 10 != x % 10)]
    
    return d17


def p43h2(acc, lst):
    if(len(lst) == 0):
        return acc
    toAdd = lst[0]
    rest = lst[1:]
    newAcc = []
    for a in acc:
        for t in toAdd:
            t = str(t)
            if(len(t) == 2):
                t = "0" + t
            if(len(a) < 3):
                appended = a + str(t)
                nunique = len(set(item for item in appended))
                if(len(appended) == nunique):
                    newAcc.append(a + t)
            else:
                if(a[-2] == t[0] and a[-1] == t[1] and t[2] not in a):
                    newAcc.append(a + t[2])
    return p43h2(newAcc, rest)

def p43():
    #factors = [2,3]
    factors = [2,3,5,7,11,13,17]
    nums = [p43helper(i) for i in factors]
    nums.insert(0, range(0,10))
    allVals = p43h2([""], nums)
    print(sum([int(x) for x in allVals]))


def p52():
    """It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """
    for i in range(10, 1000000):
        criteria = [3, 4, 5]
        first = sorted(str(2 * i))
        compare = [sorted(str(i * x)) for x in criteria]
        if all(first == x for x in compare):
            return i

def isBouncy(n):
    ns = str(n)
    nss = ns[0]
    for i in range(1, len(ns)):
        if(ns[i] != nss[-1]):
            nss += ns[i]

    ns = nss
    for i in range(1,len(ns) - 1):
        if(ns[i-1] < ns[i] and ns[i+1] < ns[i]):
            return True
        if(ns[i-1] > ns[i] and ns[i+1] > ns[i]):
            return True
    return False

def numBouncy(n, prevCount):
    if(isBouncy(n)):
        return prevCount + 1
    return prevCount

def p112():
    bouncy = 0
    for i in range(1,10000000):
        bouncy = numBouncy(i, bouncy)
        if(bouncy / float(i) == 0.99 ):
            print(f"i: {i} bouncy: {bouncy}")
            return

def david():
    ''' I have no idea what this is...
    '''
    n = 142857 + 1587000

    s = str(n)

    cipher = [3,25,3,31,13,23,32]
    answer = []

    for i in range(len(cipher)):
        answer.append(chr(ord('a') + cipher[i] - int(s[i]) - 1))

        print("".join(answer))

def p44():
    '''Project euler problem 44
    Pentagonal numbers are generated by the formula, Pn=n(3n - 1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
    '''
    pentagonalNumbers = [x * (3 * x - 1) / 2 for x in range(1, 5000)]
    print(pentagonalNumbers[0:100])
    minD = 1000000
    for j, pj in enumerate(pentagonalNumbers):
        for k,pk in enumerate(pentagonalNumbers):
            if(k < j):
                continue
            if pk + pj in pentagonalNumbers:
                if pk - pj in pentagonalNumbers:
                    print("pj: {}, pk: {}, dif: {}".format(pj, pk, abs(pk - pj)))
                    if(abs(pk - pj) < minD):
                        minD = abs(pk - pj)

    print("minD: {}".format(minD))

from collections import defaultdict
def p45():
    dct = defaultdict(lambda:0)
    for i in range(100000):
        t = triangle_number(i)
        p = pentagonal_number(i)
        h = hexagonal_number(i)
        for j in [t,p,h]:
            dct[j] = dct[j] + 1
            if dct[j] >= 3:
                print(j)

def p46():
    primes = primesUpTo(10000)
    squares = [x**2 for x in range(1, 100)]
    vals = {x:False for x in range(5, max(primes) + 2 * max(squares), 2)}
    for p in primes:
        vals[p] = True
        for s in squares:
            vals[p + 2 * s] = True
    left = [k for (k,v) in vals.items() if not v]
    print(min(left))

def prime_factorization(n, primes_list, acc):
    if (n in primes_list):
        return [n]
    for p in primes_list:
        if n % p == 0:
            return [p] + prime_factorization(n / p, primes_list, acc + 1)


def p47():
    '''
    Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?'''
    mx = 200000
    consec_count = 4
    print("getting primes up to {}".format(mx))
    primes = primesUpTo(mx)
    factor_table = {}
    print("getting prime factorization...")
    for i in range(2,mx):
        print(i)
        unique_factors = set(prime_factorization(i, primes, 0))
        if not len(unique_factors) in factor_table:
            factor_table[len(unique_factors)] = []
        factor_table[len(unique_factors)].append(i)
    print("finding desirable factors...")
    desired_factors = np.array(factor_table[consec_count])
    print(desired_factors)
    difference_between = desired_factors[consec_count -1:] - desired_factors[:-(consec_count - 1)]
    index = np.argmax(difference_between == consec_count - 1)
    print (index)
    print (desired_factors[index])


def p48():
    ''' Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000. '''
    modMe = pow(10,10)
    result = 0
    for i in range(1,1001):
        toAdd = i
        for p in range(i - 1):
            toAdd = (toAdd * i) % modMe
        result = (result + toAdd) % modMe
        print(f"{i}, {toAdd}, {result}")

    print(result)

def p49():
    '''
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
    '''
    # find all 4 digit primes
    primes = [x for x in primesUpTo(10000) if x > 1000]
    prime_digit_sets = [''.join(sorted(list(str(x)))) for x in primes]
    result = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if(prime_digit_sets[i] != prime_digit_sets[j]):
                continue
            for k in range(j + 1, len(primes)):
                if(prime_digit_sets[i] != prime_digit_sets[k]):
                    continue
                if(primes[j] - primes[i] == primes[k] - primes[j]):
                    result.append((primes[i], primes[j], primes[k]))
    print(result)

def p50():
    ''' Largest sum of consecutive primes
    The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
    '''
    from collections import deque
    primes_below_one_mil = primesUpTo(1000000)

    inspect_list = deque()
    inspect_list.append(primesUpTo(4000))
    done = False
    examined = set()

    while len(inspect_list) > 0:
        to_inspect = inspect_list.popleft()
        print([len(to_inspect), sum(to_inspect)])
        s = sum(to_inspect)
        if s in primes_below_one_mil:
            return s;
        inspection_candidate = to_inspect[1:]
        inspection_candidate_s = "%d,%d" % (inspection_candidate[0], inspection_candidate[-1])
        if inspection_candidate_s not in examined:
            inspect_list.append(inspection_candidate)
            examined.add(inspection_candidate_s)

        inspection_candidate = to_inspect[:-1]
        inspection_candidate_s = "%d,%d" % (inspection_candidate[0], inspection_candidate[-1])
        if inspection_candidate_s not in examined:
            inspect_list.append(inspection_candidate)
            examined.add(inspection_candidate_s)
                

    print("no consecutive primes summing to prime found!!")

def p53():
    '''How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?'''
    count = 0
    for n in xrange(1, 101):
        for r in xrange(1, n):
            if(nChooseR(n, r) > 1000000):
                count+=1
    print(count)

if __name__ == '__main__':
    p53()
        
