__author__ = 'julenka'

import numpy as np
import time
from primes import get_totient


def is_perm(a,b):
    """ Return if a is a permutation of b

    :param a:
    :param b:
    :return:
    """
    return sorted(str(a)) == sorted(str(b))


if __name__ == "__main__":
    n = 10**7
    s1 = time.time()
    totients = np.zeros(n, np.int32)
    get_totient(totients)
    s2 = time.time()
    print("get_totients: {}s".format(s2 - s1))
    ratio_phi_n = []
    n_values = []
    for i, t in enumerate(totients):
        if is_perm(i,t) and i > 1:
            # append n/phi(n)
            ratio_phi_n.append(float(i)/t)
            n_values.append(i)
    s3 = time.time()

    print("find_minimum: {}s".format(s3 - s2))
    min_i = np.argmin(ratio_phi_n)
    print ratio_phi_n
    print n_values[min_i]

