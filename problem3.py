

def main(num):
    num_add = 1
    i = 1

    while True:
        if num % i == 0:
            num_add *= i
            if num_add == num:
                break
        i += 1

    print(i)


if __name__ == '__main__':
    main(600851475143)