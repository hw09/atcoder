N, X = map(int, input().split())
L = [int(x) for x in input().split()]
ans = 1
D = 0
for i in range(N):
    D += L[i]
    if D <= X:
        ans += 1
print(ans)