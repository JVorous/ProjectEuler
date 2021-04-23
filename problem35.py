'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
_____
Observations
if n, of length k with k > 1, is circular prime than all the digits of n must themselves be prime
IE: all circular primes greater than 1 digit are composed of the digits 1,3,5,7,9 -- it has no even digits
'''

import time
from problem27 import list_primes


def has_even_digits(n):
    for d in str(n):
        if int(d) % 2 == 0:
            return True
    return False


#returns all rotations of a number, n, but does not return n itself
def rotate(input):
    for _ in range(len(input)-1):
        input = input[1:] + input[0]
        yield int(input)


def is_circular(n):
    if len(str(n)) < 2:
        return True
    elif has_even_digits(n):
        return False
    else:
        for x in rotate(str(n)):
            if int(x) not in my_primes:
                return False
    return True


if __name__ == '__main__':
    #driver code
    start_time = time.time()

    my_primes = list_primes(1000000)
    circ_count = 0

    for p in my_primes:
        if is_circular(p):
            circ_count += 1

    print(circ_count)
    print('Runtime: {}'.format(time.time() - start_time))
