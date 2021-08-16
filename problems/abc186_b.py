H, W = map(int, input().split())

A = []
minv = 1000
for _ in range(H):
    a = list(map(int, input().split()))
    minv = min(minv, min(a))
    A.append(a)

ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j] - minv

print(ans)
