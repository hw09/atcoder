import math

N, D = map(int, input().split())
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    d = math.sqrt(x**2 + y**2)
    if D >= d:
        ans += 1
print(ans)
