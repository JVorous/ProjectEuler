'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an
integer with (1,2, ... , n) where n > 1?

_______________

OBSERVATIONS

assume x is some integer, of length 5, that satisfies the demand -- thus there exists a series of consecutive
values (1, 2,...n) with n > 1.
but the concatenated product of the first values -- X*1 and X*2 will be 10 digits in length.
a 10 digit number cannot be 1 - 9 pandigital.

thus x will have max length of 4 digits.
'''

import time

def is_pandigital(a, l):
    check_list = [x for x in range(1,l+1)]

    if len(a) == len(set(a)):
        counter = 0
        for x in a:
            if int(x) in check_list:
                counter += 1
        if counter == l:
            return True

def can_pandigit(n):
    prod_string = ''
    done = False
    int_list = []
    x = 1
    while not done:
        prod_string += str(n*x)
        if is_pandigital(prod_string, 9):
            done = True
        if len(prod_string) > 9:
            break
        else:
            x += 1
    return done, int(prod_string)

#driver code
if __name__ == '__main__':
    start_time = time.time()
    curr_max = 0
    n = 1
    while len(str(n)) < 5:
        a, b = can_pandigit(n)
        if a:
            if curr_max < b and len(str(b)) < 10:
                curr_max = b
        n += 1

    print(curr_max)
    print('Runtime: {}'.format(time.time() - start_time))