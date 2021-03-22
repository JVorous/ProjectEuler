
def main(targ):
    numList = [1, 1]
    while True:
        numList.append(numList[-2] + numList[-1])
        if len(str(numList[-1])) == targ:
            break

    print(len(numList), end=': ')
    print(numList[-1])


if __name__ == '__main__':
    main(1000)
