
def main():
    reg_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    week_day = 2
    sunday_count = 0

    #calculate the start date of each month
    #if that day is on a sunday then count it
    for i in range(1901, 2001):
        for j in range(0, 12):
            if i % 4 != 0:
                week_day += reg_days[j] % 7
            else:
                week_day += leap_days[j] % 7

            if week_day % 7 == 0:
                sunday_count += 1

    print(sunday_count)


if __name__ == '__main__':
    main()
