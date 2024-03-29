'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

import time
import math
from problem44 import is_pentagonal

def is_hexagonal(n):
    if (math.sqrt(8*n + 1) + 1) % 4 == 0:
        return True

def gen_triangle(n):
    return (n*(n+1))/2

#driver code
if __name__ == '__main__':
    start_time = time.time()
    foundIt = False

    n = 285
    while not foundIt:
        n += 1
        b = gen_triangle(n)
        if is_hexagonal(b) and is_pentagonal(b):
            foundIt = True

    print(int(b))
    print('Runtime: {}'.format(time.time() - start_time))