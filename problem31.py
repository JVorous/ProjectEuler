#Obesrvations
# There is 1 way to reach 200p with each coin denomination (200 1p, 100 2p, 40 5p, etc)
# starting with 1p you have 1 way to make 200p
# starting with 1p and 2p you have all the ways using just the 1p to make 200, plus some new ways using 2p
# add in a 5p, and you have all the ways using the 1p and 2p, plus some new ways using the 5p coin.
#build 'matrix' of combinations following above logic -- bottom right square will hold the value

import numpy as np

def sums(l, targ):
    #create matrix to hold possible coin combinations
    #include option for "using 0 coins" and set it to 1. This is so the column combinations add up
    a = np.zeros((len(l)) * (targ+1), dtype=int).reshape((len(l)),(targ+1))
    for row in range(a.shape[0]):
        a[row][0] = 1

    for row in range(len(l)):
        currentCoin = l[row]
        for col in range(1,a.shape[1]):
            #for each matrix index, sum value above and
            a[row][col] = a[row-1][col] + a[row][col-currentCoin]

    print(a[a.shape[0]-1][a.shape[1]-1])

if __name__ == '__main__':
    my_list = [0, 1, 2, 5, 10, 20, 50, 100,200]
    sums(my_list, 200)

