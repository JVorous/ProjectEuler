def sum_factors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def is_abund(n):
    if sum_factors(n) > n:
        return True

def main(n):
    #list of whether or not each numerical index is sum of 2 abundant numbers
    num_list = [False] * (n)

    #list of all abundant numbers
    abund_list = [x for x in range(n) if is_abund(x)]

    #loop through list of abundant numbers
    #mark indices of num_list as True if it is sum of two abundants
    for i in abund_list:
        for j in abund_list:
            if i + j < n:
                num_list[i+j-1] = True
            else:
                break

    #sum remaining values
    result = 0
    for i in range(1, n):
        if num_list[i-1] == False:
            result += i

    print(result)




if __name__ == '__main__':
    main(28123)