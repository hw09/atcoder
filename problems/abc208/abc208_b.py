import math
P = int(input())

p = P
ans = 0
for i in reversed(range(1, 11)):
    d = divmod(p, math.factorial(i))
    ans += d[0]
    p = d[1]
    if p == 0:
        break

print(ans)
