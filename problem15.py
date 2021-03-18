# This can be perceived as a question related to pascal's triangle and rephrased as:
# how many different combinations of steps are there to go from (0,0) to (20,20)
# -- https://en.wikipedia.org/wiki/Pascal%27s_triangle
# reduces to a "n choose x" question.

from math import factorial


def main(a,b):
    print(int(factorial((a + b)) / (factorial(a)*factorial(b))))


if __name__ == '__main__':
    main(20, 20)
