numDict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
           6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
           11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
           15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
           19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
           50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
           90: 'Ninety', 1000: 'OneThousand', 'hundred': 'Hundred', 'And': 'and'}

def convert(n):
    try:
        return numDict[n]
    except KeyError:
        if n < 100:
            return (numDict[n - n % 10] + numDict[n % 10].lower())
        else:
            a = 100
            b = n // 100
            c = n - b * a
            if c == 0:
                return ((numDict[b] + numDict['hundred']).lower())
            else:
                return ((numDict[b] + numDict['hundred'] + numDict['And'] + convert(c)).lower())


def main():

    letterCount = []

    for i in range(1, 1001):
        letterCount.append(len(convert(i)))

    print(sum(letterCount))


if __name__ == '__main__':
    main()
