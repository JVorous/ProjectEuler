'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


___________
OBSERVATIONS

writing out the first few sequences gives (spaces are just for illustrative purposes):
123456789 1011121314151617181920212223242526272829...90919293949596979899 100101102103104105106107018109...

thus the block of single digits is 9 numbers  -- 1*9 = 9 digits
the block of 2 digits has 90 numbers          -- 2*90 = 180 digits
the block of 3 digits has 900 1 digit numbers -- 3 * 900 = 2700 digits
etc


'''

import time

def get_digit(n):
    digits = 1
    skip = 0
    num_block = 9

    #determine which "block" (1 digit, 2 digit, 3 digit, etc) contains target position
    while skip + digits*num_block < n:
        skip += digits*num_block
        num_block *= 10
        digits += 1

    #skip all the "blocks" before the position's block
    idx = 10**(digits-1)
    num_str = ''

    # build number block until the target n-position is included
    while len(str(idx)) == digits:
        num_str += str(idx)
        if len(num_str) <= n - skip:
            idx += 1
        else:
            break
    return int(num_str[n - skip - 1])

#driver code
if __name__ == '__main__':
    start_time = time.time()
    output = 1

    for i in range(7):
        output *= get_digit(10**i)

    print(output)
    print('Runtime: {}'.format(time.time() - start_time))