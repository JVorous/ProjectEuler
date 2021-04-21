from fractions import Fraction

def main():
    a = 10
    b = 10
    fract_list = set()
    while len(str(a)) < 3:
        if a % 10 != 0 and b % 10 != 0 and a /b < 1:
            red_a = 0
            red_b = 0
            #check if a and b are of non-trivial format
            str_a = str(a)
            str_b = str(b)
            #refactor this - could be simpler
            if str_a[0] == str_b[0]:
                red_a = int(str(a)[1])
                red_b = int(str(b)[1])
            elif str_a[0] == str_b[1]:
                red_a = int(str(a)[1])
                red_b = int(str(b)[0])
            elif str_a[1] == str_b[0]:
                red_a = int(str(a)[0])
                red_b = int(str(b)[1])
            elif str_a[1] == str_b[1]:
                red_a = int(str(a)[0])
                red_b = int(str(b)[0])

            #check that non-trivial reduced fractions were found
            if red_a != 0 and red_b != 0:
                if a / b == red_a / red_b:
                    fract_list.add((red_a, red_b))

        #per conditions, both a and b are 2-digit values
        if len(str(b)) < 3:
            b += 1
        else:
            b = 10
            a += 1

    fraction_prod = Fraction(1,1)
    for a, b in fract_list:
        fraction_prod *= Fraction(a,b)

    print('The numerator is {} and the denominator is {}'.format(fraction_prod.numerator, fraction_prod.denominator))

if __name__ == '__main__':
    main()