N, M, C = map(int, input().split())
B = [int(x) for x in input().split()]
ans = 0
for i in range(N):
    A = [int(y) for y in input().split()]
    S = 0
    for j in range(M):
        S += A[j] * B[j]
    if S + C > 0:
        ans += 1
print(ans)

