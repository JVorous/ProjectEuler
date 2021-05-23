'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
######
OBSERVATIONS

what is being asked is to find the (1^1 + 2^2 + 3^3 + ... + 1000^1000) mod 10^10

that's equivalent to 1^1 mod 10 + 2^2 mod 10 + 3^3 mod 10 + .... 1000^1000 mod 10
'''


import time

def power_mod(a, b, mod):
    return a**b % mod

# driver code
if __name__ == '__main__':
    start_time = time.time()
    mod = 10**10
    output = 0
    for i in range(1,1001):
        output = (output + power_mod(i, i, mod)) % mod

    print(output)

    print('Runtime: {}'.format(time.time() - start_time))