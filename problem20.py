from math import factorial

def main(n):
    num_list = list(str(factorial(n)))

    print(sum(int(x) for x in num_list))

if __name__ == '__main__':
    main(100)
