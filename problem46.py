'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a
prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

____
OBSERVATIONS
for any odd composite, n, that satisfies n = p + 2x^2, where p is prime and x is a natural number
  only need study primes that are less than n-2

since both p and x are non-zero integers it follows that x is strictly less than (n/2)^.5
'''

import time
import math
from problem27 import list_primes, is_prime


def gold_num(n):
    prime_list = list_primes(n - 2)
    is_gold_num = False
    for k in range(1, int(math.sqrt(n / 2) + 1)):
        p = n - 2*k**2
        if p in prime_list:
            is_gold_num = True
            break

    return is_gold_num


# driver code
if __name__ == '__main__':
    start_time = time.time()
    done = False
    n = 33

    while not done:
        n += 2
        if not is_prime(n) and not gold_num(n):
            done = True

    print('Result: {}'.format(n))
    print('Runtime: {}'.format(time.time() - start_time))
