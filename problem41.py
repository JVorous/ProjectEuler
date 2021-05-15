'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
______
OBSERVATIONS
let x be an n-digit pandigital prime.
then by definition x has n-digits
and the largest value x could have would be less than 10 digits -- 10 digit numbers cannot be pandigital
x has upper bound of 987654321 -- any higher value is not 9-digit pandigital
'''

import time
from problem38 import is_pandigital
from problem27 import list_primes


#driver code
if __name__ == '__main__':
    start_time = time.time()
    curr_max = 2

    prime_list = list_primes(8000000)

    for n in prime_list:
        if is_pandigital(str(n), len(str(n))):
            if n > curr_max:
                curr_max = n

    print(curr_max)
    print('Runtime: {}'.format(time.time() - start_time))