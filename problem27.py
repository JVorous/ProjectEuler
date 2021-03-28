#observation
# if the expression n^2 + an + b results in a prime number for consecutive values of n starting at n = 0
# then, as evidenced by the case of n = 0, b itself must be prime.
# thus -- only use prime values between 2 and 1000 for b

import math


def list_primes(n):
    #initiate list of n true booleans
    nums = [True] * (n + 1)
    prime_nums = []
    #first and second index represent 0 and 1 -- neither are prime, set their index to False
    nums[0] = nums[1] = False

    #for each key-value in the list, calculate primeness
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            prime_nums.append(i)
            #set multiples of current prime to False
            for x in range(i * i, n + 1, i):
                nums[x] = False

    return prime_nums


def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0 and n != 2:
            return False

    return True


def main():
    b = list_primes(1000)

    max_count = 0
    coef1 = 0
    coef2 = 0


    for a in range(-1000, 1001):
        for val in b:
            counter = 0
            done = False
            n = 0
            while not done:
                test_val = n**2 + a*n + val

                if test_val > 0 and is_prime(test_val):
                    counter += 1
                    n += 1
                else:
                    done = True

            if max_count < counter:
                max_count, coef1, coef2 = counter, a, val

    print('Max count is {} primes for coefficients a = {} and b = {}'.format(max_count, coef1, coef2))
    print('The coefficient product is: {}'.format(coef1 * coef2))


if __name__ == '__main__':
    main()



