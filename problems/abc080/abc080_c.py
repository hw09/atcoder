N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -10**10

for b in range(1, 2**10):
    ch = [0] * N
    for i in range(10):
        if (b>>i) & 1:
            for j in range(N):
                ch[j] += F[j][i]
    ma = 0
    for k in range(N):
        ma += P[k][ch[k]]
    ans = max(ans, ma)
print(ans)
