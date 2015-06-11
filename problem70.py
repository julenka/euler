__author__ = 'julenka'

import numpy as np
import time
import euler_utils

n = 10**7

def is_perm(a,b):
    """ Return if a is a permutation of b

    :param a:
    :param b:
    :return:
    """
    return sorted(str(a)) == sorted(str(b))


def get_totient(phi):
    """ Compute totient(i) for i in range(n) and stick it in phi

    Copied from http://codegolf.stackexchange.com/questions/26739/super-speedy-totient-function

    :param phi:
    :return:
    """
    s = 0

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

if __name__ == "__main__":
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

