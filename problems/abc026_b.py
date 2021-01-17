import math
n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += r[i]**2 * math.pi
    else:
        ans -= r[i]**2 * math.pi
print(ans)