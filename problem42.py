'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

______
OBSERVATIONS

There are only 26 letters in the English alphabet, so you only need the first 26 triangle numbers
create list of first 26 triangle numbers
create a list of each English alphabet letter, the index in the list is the letter's "value" (offset by 1)
sum indices of each letter in each word and check for existance in the list of triangle numbers
'''

import time

def get_tri_nums():
    return [int((x*(x+1))/2) for x in range(1,27)]

#driver code
if __name__ == '__main__':
    start_time = time.time()
    alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tri_num_list = get_tri_nums()
    tri_word_count = 0

    with open('res\p042_words.txt') as f:
        word_list = [x.replace('"','') for x in f.read().split(',')]

    for word in word_list:
        total = 0
        for char in word:
            total += alpha_list.index(char.upper()) + 1

        if total in tri_num_list:
            tri_word_count += 1

    print(tri_word_count)
    print('Runtime: {}'.format(time.time() - start_time))