'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

#####
OBSERVATIONS

let n be one term of this 4-digit increasing sequence.
then no digit n_i of n can be 0 since on permutation it would produce a non-4-digit term, which would not be increasing

'''

import time
from problem27 import is_prime

def has_blocked_digits(n):
    return '0' in str(n)

def permutations(val, perm_set, step = 0):
    if step < len(val):
        for i in range(step, len(val)):
            # copy the string (store as array to swap indices)
            perm_string = [c for c in val]

             # swap the current index with the step
            perm_string[step], perm_string[i] =perm_string[i], perm_string[step]

            #rejoin into integer
            term = int("".join(perm_string))
            if is_prime(term):
                perm_set.add(term)
             # recurse on the portion of the string that has not been swapped yet
            permutations(perm_string, perm_set, step + 1)

    return perm_set

def prime_perms(n):
    my_seq = set()
    perm_list = permutations(str(n), my_seq)
    perm_list.remove(n)
    for perm in perm_list:
        b = perm + (perm - n)
        if b in perm_list:
            return [n, perm, b]

    return []


#Driver code
if __name__ == '__main__':
    start_time = time.time()
    done = False
    n = 999
    seq = []
    while not done:
        n += 1
        if not has_blocked_digits(n) and is_prime(n):
            seq = prime_perms(n)

        if len(seq) == 3 and 1487 not in seq:
            done = True


    print(''.join(map(str, seq)))
    print("Runtime: {}".format(time.time() - start_time))