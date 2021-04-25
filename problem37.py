'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

________________
Observations:

let n be a k-length truncatable prime.
let x be some trunctated value of n (with less than k digits) -- if x is a multiple of 2 or 5 than x is not prime.
so n must *NOT* have any truncated values which are multiples of 2 or 5.
'''

from problem27 import is_prime
import time


def has_blocked_digits(n):
    d = int(str(n)[1:])
    while d:
        if d % 2 == 0 or d % 5 == 0:
            return True
        else:
            d //= 10

    return False


def left_trunc(p):
    tmp_str = str(p)
    if len(tmp_str) > 1:
        p = int(tmp_str[1:])
        if is_prime(p):
            return left_trunc(p)
        else:
            return False
    else:
        if is_prime(p) and p >= 2:
            return True

def right_trunc(p):
    if len(str(p)) > 1:
        p //= 10
        if is_prime(p):
            return right_trunc(p)
        else:
            return False
    else:
        if is_prime(p) and p >= 2:
            return True

def prime_trunc(n):
    if has_blocked_digits(n):
        return False
    elif is_prime(n):
        if right_trunc(n):
            return left_trunc(n)


#driver code
if __name__ == '__main__':
    start_time = time.time()

    trunc_list = []
    n = 9

    while len(trunc_list) < 11:
        n += 1
        if prime_trunc(n):
            trunc_list.append(n)

    print(sum(trunc_list))
    print('Runtime: {}'.format(time.time() - start_time))
