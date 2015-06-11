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

def get_totient(phi):
    """ Compute totient(i) for i in range(n) and stick it in phi

    Copied from http://codegolf.stackexchange.com/questions/26739/super-speedy-totient-function

    :param phi:
    :return:
    """
    s = 0

    n = len(phi)
    phi[1] = 1

    i = 2
    while i < n:
        if phi[i] == 0:
            phi[i] = i - 1

            j = 2

            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1

                    while q % i == 0:
                        f *= i
                        q //= i

                    phi[i * j] = f * phi[q]
                j += 1
        i += 1