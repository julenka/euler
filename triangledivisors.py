import math
def numDivisors(n):
    factor = 1
    result = 0
    while factor <= math.sqrt(n):
        if(n % factor == 0):
            result += 2
        factor += 1
    print "Num Divisors of %i is %i" % (n, result)
    return result

triNumber = 1
triIter = 2
while numDivisors(triNumber) < 500:
    triNumber += triIter
    triIter += 1

print triNumber

