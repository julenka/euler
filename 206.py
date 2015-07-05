# coding=utf-8
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
__author__ = 'julenka'

# max value is 10 ^ 20, search up to 11^
MIN_VAL = 10 ** 9
MAX_VAL = 1414213562

def matches(n):
    s=str(n)
    print s, s[::2], len(s)
    return len(s) == 19 and s[::2] == "1234567890"

for i in xrange(MIN_VAL, MAX_VAL, 10):
    if matches(i**2):
        print i, i**2
        exit(0)

print "no match found"
exit(1)

