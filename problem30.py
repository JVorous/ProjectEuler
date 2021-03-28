#observation
# let N be a generic n digit number that can be written as the sum of the 5th powers of it's digits
# where each digit is between 0 and 9 -- then the upper bound on the length (n) of N is n*9^5
# N must also be 5 digits in length thus if we go to 6 digits -- or 6*9^5 = 354294 then we've exhausted all possible N values.
# thus 354294 must be the upper bound of all numbers that fit this definition of N.

def fifth_power():
    powers = []
    for n in range(2, 354295):
        output = 0
        val = sum(int(x)**5 for x in list(str(n)))
        if val == n:
            powers.append(n)
    return powers

if __name__ == '__main__':
    list = fifth_power()
    print(sum(list))
