'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

OBSERVATIONS:

Assume some number n, of length k, qualifies as a 'curious number'. then let n_x be some digit of n.
then the # of digits in n_x! is at most k. If it is larger than k than the sum of all the digits of n would be
a value greater than k.

note that for the number 9999999 ( 7 digits) the length sum  of the factorial digits = 7
also note that for the number 99999999 (8 digits) the sum of the of the factorial digits is also 7

thus 9999999 is an upper bound on n.

'''

import math
import time

#create dictionary of factorial values so we don''t need to re-calc them a bunch
my_dict ={}
for i in range(10):
    my_dict[str(i)] = math.factorial(i)


def sum_factorials(n):
    return sum([my_dict[x] for x in list(str(n))])



#driver code
start_time = time.time()
num_list = []


for i in range(3, 9999999):
    if sum_factorials(i) == i:
        num_list.append(i)

print(sum(num_list))
print('Runtime: {}'.format(time.time() - start_time))