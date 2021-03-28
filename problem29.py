
def main(x, y):
    num_seq = set()
    for a in range(2, x+1):
        for b in range(2, y+1):
            num_seq.add(a**b)

    return num_seq


if __name__ == '__main__':
    val = main(100, 100)
    print('the # of distinct values is {a}'.format(a = len(val)))
