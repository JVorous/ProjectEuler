
def main(n):
    #initialize "center" point in matrix -- it's a diagonal so store value of 1

    x, y = 0, 0
    dx, dy = 0, 1
    diags = [1]

    for num in range(2, n**2+1):
        x, y = x + dx, y + dy
        if abs(x) == abs(y):
            diags.append(num)

        if x == y:
            #upper left and lower right corners
            if -n//2 < x <= 0:
                 dx, dy = 0, 1
            else:
                dx, dy = 0, -1
        else:
            #lower left corner
            if abs(x) == abs(y) and -n//2 <= y < 0:
                dx, dy = dy, dx

        #upper right corner
        if abs(x) == y - 1 and x <= 0:
            dx, dy = dy, dx


    print(sum(diags))

if __name__ == '__main__':
    main(1001)