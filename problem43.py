'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

'''

import time
from itertools import permutations as perms


def sub_string_divide(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    num_list = [x for x in n]
    for d in range(0,7):
        if int(num_list[d+1]+num_list[d+2]+num_list[d+3]) % divisors[d] != 0:
            return False
    return True


#driver code
if __name__ == '__main__':
    start_time = time.time()
    sum_total = 0

    for x in perms('0123456789'):
        pand = ''.join(x)
        if sub_string_divide(pand):
            sum_total += int(pand)

    print(sum_total)
    print('Runtime: {}'.format(time.time() - start_time))
