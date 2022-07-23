import sys
import math
a, b = map(int, input().split())

ans = ('-1')

for i in range(10001):
    z8 = math.floor(i * 0.08)
    z10 = math.floor(i * 0.1)

    if z8 == a and z10 == b:
        ans = i
        break

print(ans)
