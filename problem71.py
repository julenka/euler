""" Project Euler problem 71 """
__author__ = 'julenka'

import collections
import euler_utils

def get_relprime(n):
    """ Compute all values relatively prime to n
    """

    s = 0

    phi = collections.defaultdict(list)
    phi[1] = [1]

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

from fractions import Fraction

def farey(limit, n, d, N, D):
    '''Fast computation of Farey sequence as a generator

    http://www.quora.com/What-are-the-fastest-algorithms-for-generating-coprime-pairs

    '''
    # n, d is the start fraction n/d (0,1) initially
    # N, D is the stop fraction N/D (1,1) initially
    pend = []
    while True:
        mediant_d = d + D
        if mediant_d <= limit:
            mediant_n = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield Fraction(n, d)
            if pend:
                n, d, N, D = pend.pop()
            else:
                break

if __name__ == '__main__':
    limit = 1000
    n,d = (2,5)
    while limit <= 1000000:
        f=max(farey(limit, n,d, 3, 7))
        n,d=f.numerator,f.denominator
        limit *= 10
        print limit, n, d
