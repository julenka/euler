__author__ = 'julenka'
"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""

def reverse(n):
    return int(str(str(n)[::-1]))

def ndigits(n):
    result = 1
    while n >= 10:
        n /= 10
        result += 1
    return result

def allodd(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n /= 10
    return True

total = 0
cur_len = 2
print "here"
for i in xrange(10, 10 ** 9):
    if ndigits(i) > cur_len:
        cur_len = ndigits(i)
        print "10^{}".format(cur_len)


    if i % 10 ** 5 == 0:
        print i
    if i % 10 == 0:
        continue
    if allodd(i + reverse(i)):
        total += 1
print total

# print reverse(409)
# print reverse(36)
# print allodd(13)
# print allodd(4)
# print allodd(24)
