from functools import reduce
import math

def calc_factors(num):

    step = 2 if num % 2 else 1

    #List all factors up to the square root
    #include both the factor and the division output
    #produces a list of lists
    numList = [[i, num // i] for i in range(1, int(math.sqrt(num)) + 1, step) if num % i == 0]

    #reduce the above list of lists, remove duplicates, and return
    return set(reduce(lambda a, b: a + b, numList))


def main(num):
    i = 1
    while True:
        curr_sum = sum(range(i + 1))
        factorList = list(calc_factors(curr_sum))

        if len(factorList) > num:
            print(curr_sum)
            break
        else:
            i += 1


if __name__ == '__main__':
    main(500)
