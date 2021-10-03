import math
import latexify
import random


@latexify.with_latex
def solve(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

# print(solve(2,30,5))
print(solve)

for a in range(10000000):
    b = int(str(a)[::-1])
    print(a,b,a-b)
    if (a-b)%9 != 0:
        print((a-b)%9)

print("end")