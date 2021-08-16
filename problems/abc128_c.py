N, M = map(int, input().split())

S = [list(map(int, input().split()))[1:] for i in range(M)]
P = list(map(int, input().split()))

ans = 0

for sw in range(2**N):
    ch = [False] * M
    for i in range(M):
        cnt = 0
        for j in S[i]:
            if sw >> (j-1) & 1:
                cnt += 1
        if cnt % 2 == P[i]:
            ch[i] = True
        else:
            ch[i] = False

    if all(ch):
        ans += 1

print(ans)