
import re


def combine_rows(rows):
    result = []
    for x in rows[0]:
        idx = rows[0].index(x)
        a = x + rows[1][idx]
        b = x + rows[1][idx+1]
        if a > b:
            result.append(a)
        else:
            result.append(b)
    return result


def main():
    raw_tri = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    str_list = [x.strip().split(' ') for x in re.split('\n', raw_tri)]
    num_list = []

    for y in str_list:
        num_list.append([int(x) for x in y])

    while True:
        #calculate max sums of bottom two rows
        new_row = combine_rows(num_list[-2:])

        #replace bottom two rows with new summation row
        for x in num_list[-2:]:
            num_list.remove(x)
        num_list.append(new_row)

        #when single row is left it will have a single value -- the target value
        if len(num_list) == 1:
            targ_val = num_list[0][0]
            break

    print(targ_val)

if __name__ == '__main__':
    main()
