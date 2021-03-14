
def main(num):

    squareSum = sum([x for x in range(1, num+1)])**2
    sumSquares = sum([x**2 for x in range(1, num+1)])

    print(abs(squareSum - sumSquares))


if __name__ == '__main__':
    main(100)