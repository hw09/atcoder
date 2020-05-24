import itertools
n, m, x = map(int, input().split())
a = []
ans = 12 * 10**6
flg = False
for i in range(n):
    a.append([int(x) for x in input().split()])
for j in range(1, n+1):
    for z in itertools.combinations([y for y in range(1, n+1)], j):
        A = [0]*m
        M = [False]*m
        for k in range(m):
            C = 0
            for zz in z:
                C += a[zz-1][0]
                A[k] += a[zz-1][k+1]
                if A[k] >= x:
                    M[k] = True
            if False not in M:
                if ans > C:
                    ans = C
                    flg = True
if flg:
    print(ans)
else:
    print(-1)