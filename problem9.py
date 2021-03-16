def main():

    for a in range(1, 1000):
        for b in range(1, 1000):
            c = ((a * a) + (b * b)) ** (1 / 2)
            if (a + b + c) == 1000:
                prod = int(a * b * c)

    print(prod)


if __name__ == '__main__':
    main()
