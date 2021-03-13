def check_palindrome(num):
    arr = list(str(num))
    if arr == arr[::-1]:
        return True

def main():
    a = 100
    numList = []

    while len(str(a)) < 4:
        for x in range(100, 1000, 1):
            prod = a * x
            if check_palindrome(prod):
                numList.append(prod)
        a += 1

    print(max(numList))



if __name__ == '__main__':
    main()