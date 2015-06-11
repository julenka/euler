#!/usr/bin/env python

"""
    Utilities for dealing with primes
"""
import numpy


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n 

        Credit: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

