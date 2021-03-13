def main(count):
    num = 1
    for i in (range(1, count + 1)):
        if num % i > 0:
            for j in range(1, count + 1):
                if (num * j) % i == 0:
                    num *= j
                    break
    print(num)


if __name__ == '__main__':
    main(20)
