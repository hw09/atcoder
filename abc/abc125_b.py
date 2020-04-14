N = int(input())
V = [int(x) for x in input().split()]
C = [int(y) for y in input().split()]
ans = 0
for i in range(N):
    t = V[i] - C[i]
    if t > 0:
        ans += t
print(ans) 