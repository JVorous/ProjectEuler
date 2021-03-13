def main(max_num):
    numList = []

    a = 1
    b = 1
    while a < max_num:
        a, b = b, a + b
        if a % 2 == 0:
            numList.append(a)

    print(sum(numList))


if __name__ == '__main__':
    main(4000000)
