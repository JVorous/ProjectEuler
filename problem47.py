'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

######
OBSERVATIONS

let n be an integer with 4 distinct primes.
2 *3*5*7 = 210 -- lower bound on n
guess for first pass, calculate primes up to 1000
'''

import time
from problem27 import list_primes

def find_prime_factors(n, primes):
    my_list = []
    for i in primes:
        if n % i == 0:
            my_list.append(i)
    return my_list


# driver code
if __name__ == '__main__':
    start_time = time.time()
    fact_list = []
    prime_list = list_primes(1000)
    n = 209

    while len(fact_list) < 4:
        n += 1
        if len(find_prime_factors(n, prime_list)) == 4:
            if len(fact_list) > 0:
                if fact_list[-1] == n - 1:
                    fact_list.append(n)
                else:
                    fact_list.clear()
            else:
                fact_list.append(n)

    print(fact_list)
    print('Runtime: {}'.format(time.time() - start_time))
