from math import log, ceil


def find_primes(limit):
    # initiate list of n true booleans
    prime_dict = [True] * (limit + 1)

    #first and second index represent 0 and 1 -- neither are prime, set their index to False
    prime_dict[0] = prime_dict[1] = False

    # for each key-value in the list, calculate primeness
    for (i, is_prime) in enumerate(prime_dict):
        if is_prime:
            yield i

            # set multiples of current prime to False
            for n in range(i * i, limit + 1, i):
                prime_dict[n] = False


def upper_bound(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_n_prime(n):

    primes = list(find_primes(upper_bound(n)))

    return sum([x for x in primes if x < 2000000])


if __name__ == '__main__':
    print(find_n_prime(2000000))
