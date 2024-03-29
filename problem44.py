'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
and D = |Pk − Pj| is minimised; what is the value of D?
_____
OBSERVATION

for any arbitrary integer, n, there exists the pentagonal number Pn
thus n has no upper limit

but if you "work backwards" from any given value of n then the first target pair, Pj and Pk, that you hit
is the minimised set -- if there is no target pair for a given value of n then increment n + 1 and start
working backwards toward 0 again.

'''


import time
import math

def form_pentagonal(n):
    return int((n*(3*n-1))/2)

def is_pentagonal(n):
    if (math.sqrt(24*n+1)+1) % 6 == 0:
        return True


#driver code
if __name__ == '__main__':
    start_time = time.time()
    foundIt = False
    min_diff = 0
    j = 0
    while not foundIt:
        j += 1
        a = form_pentagonal(j)
        for k in range(j-1, 0,-1):
            b = form_pentagonal(k)
            if is_pentagonal(a + b) and is_pentagonal(a - b):
                min_diff = abs(a - b)
                foundIt = True

    print(min_diff)
    print('Runtime: {}'.format(time.time() - start_time))
