
def sum_factors(n):
    return sum([i for i in range(1, n) if n % i == 0])


def is_pair(a, b):
    if a == sum_factors(b):
        return True


def main(n):
    amicable_list = []
    for b in range(1, n):
        a = sum_factors(b)
        if is_pair(b, a) and a != b:
            amicable_list.append(a)
            amicable_list.append(b)


    #strip out duplicate values and sum the result
    print(sum(list(set(amicable_list))))


if __name__ == '__main__':
    main(10000)
