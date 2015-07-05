#!/usr/bin/env python
__author__ = 'julenka'

from collections import defaultdict

def get_digits(n):
    result = []
    while n > 10:
        result.append(n % 10)
        n /= 10
    result.append(n)
    return list(reversed(result))

codes = [get_digits(int(x)) for x in open("p079_keylog.txt").readlines()]

digits = set()
for c in codes:
    for d in c:
        digits.add(d)


# key is before values
before = defaultdict(set)
for c1,c2,c3 in codes:
    before[c1].add(c2)
    before[c1].add(c3)
    before[c2].add(c3)

order = [(len(v), k) for k,v in before.iteritems()]
answer = [ str(v) for k,v in sorted(order, reverse=True)]
# There is one digit in digits that's not in answer. Add to end
print digits, "".join(answer)