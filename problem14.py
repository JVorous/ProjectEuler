
def main():
    maxChain = []

    for x in range(1, 1000000):
        currChain = [x]

        while x > 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3*x + 1

            currChain.append(x)

        if len(currChain) > len(maxChain):
            maxChain = currChain

    print(maxChain[0])


if __name__ == '__main__':
    main()
