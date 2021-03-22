from functools import reduce
from itertools import permutations

def main(l):
    perm = permutations(l)

    # Print the obtained permutations
    for i, x in enumerate(perm):
        if i == 999999:
            print(reduce(lambda a, b: a+b, x))

if __name__ == '__main__':
    main(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
