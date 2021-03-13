

def main():
    numList = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            numList.append(i)
    print(sum(numList))


if __name__ == '__main__':
    main()

