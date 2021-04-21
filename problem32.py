"""
Observations
first, assume a X b = c is 1 - 9 pandigital, and let L(z) = lengh of z in digits. then L(a) + L(b) + L(c) = 9
there are no 0 digits, and and b are positive and have at least 1 digit -- their length is restricted by:
L(a) + L(b) - 1 <= L(c) <= L(a) + L(b)
that can be reduced to an upper bound on the length of a:

1 <= L(a) <= (d - 1) / 2 or -- L(a) is between 1 and 4, inclusive

"""

def is_pandigital(a, b, c):
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_str = str(a) + str(b) + str(c)
    if len(num_str) == len(set(num_str)):
        counter = 0
        for x in num_str:
            if int(x) in check_list:
                counter += 1
        if counter == 9:
            return True


def main():
    a = 1
    b = 1
    prod_list = set()
    while len(str(a)) <= 4:
        if is_pandigital(a, b, a*b):
            prod_list.add(a*b)
        if len(str(a)) + len(str(b)) + len(str(a*b)) <= 9:
            b += 1
        else:
            b = 1
            a += 1

    print(sum(prod_list))



if __name__ == '__main__':
    main()
