'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly
three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

______
OBSERVATIONS

since the triangle is a right triangle we can get the following equation:
a^2 + b^2 = c^2
and
a + b + c ≤ 1000
p has to be an even number
a, b, and c are all non-zero integers strictly less than p thus p//3 ≤ a ≤ p//2
'''

import time

#driver code
start_time = time.time()
max_p = 0
max_set = 0

for p in range(2, 1001, 2):
    l = []
    for a in range(p//3, p//2):
        for b in range(p - a):
                c = p - a - b
                if a**2 + b**2 == c**2:
                    curr = [a, b, c]
                    curr.sort()
                    if curr not in l:
                        l.append(curr)

    if max_set < len(l):
        max_p = p
        max_set = len(l)
    p += 1

print(max_p)
print('Runtime: {}'.format(time.time() - start_time))