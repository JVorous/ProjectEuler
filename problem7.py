from math import log, ceil


def find_primes(limit):
    #initiate list of n true booleans
    nums = [True] * (limit + 1)

    #first and second index represent 0 and 1 -- neither are prime, set their index to False
    nums[0] = nums[1] = False

    #for each key-value in the list, calculate primeness
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i

            #set multiples of current prime to False
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_p_n(n):
    #calculate upper bound for the nth prime
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_n_prime(n):
    #primes = list(find_primes(upper_bound_for_p_n(n)))
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]


if __name__ == '__main__':
    print(find_n_prime(10001))