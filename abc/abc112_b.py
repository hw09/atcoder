N, T = map(int, input().split())
ans = 10000
for _ in range(N):
    c, t = map(int, input().split())
    if T >= t:
        if ans > c:
            ans = c
print(ans if ans != 10000 else 'TLE')
