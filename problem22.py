from string import ascii_uppercase

def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))


def main():

    with open('res\p022_names.txt') as f:
        names = f.read().split(',')
        names.sort()

    print(sum(i * score(x) for i, x in enumerate(names, 1)))


if __name__ == '__main__':
    main()
