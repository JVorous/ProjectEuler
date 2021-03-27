#obervations
# the decimal notation of 1/n either has a finite number of digits after the decimal, or it repeats forever
# if the value repeats, then you can have at most n digits in the cycle before it repeats
# thus -- if you are at n+1 digits after the decimal then either you've restarted the cycle or there is no cycle.
#long division will produce a trackable cycle

def long_div(n, d, max_len):

    i = 0
    remainders = []

    #i represents the # of digits found -- as stated this at most the size of d
    while i <= max_len:

        #if n < d then we are on the right of the decimal -- multiple numerator by 10 to account for decimal shift
        if n < d:
            n = n * 10

        #calc remainder (modulus) of numerator and denominator
        #this value will become the new numerator if loop is repeated
        n = n % d

        if n in remainders:
            #n is a repeated remainder -- the cycle is complete.
            return d, i
        else:
            remainders.append(n)

        i = i + 1


def main():
    curr_denom = 0
    max_length = 0
    largest_denominator = 1000
    for x in range(2, largest_denominator + 1):
        y = long_div(1, x, x)
        if y[1] > max_length:
            curr_denom, max_length = y

    print(f'The denominator {curr_denom} produces a cycle of length {max_length} digits')


if __name__ == '__main__':
    main()
