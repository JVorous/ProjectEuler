'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time

def is_palin(n):
    return str(n) == str(n)[::-1]

#driver code
start_time = time.time()

palindromes = []

for i in range(1000000):
    if is_palin(i):
        if is_palin(bin(i)[2:]):
            palindromes.append(i)

print(sum(palindromes))
print('Runtime: {}'.format(time.time() - start_time))
