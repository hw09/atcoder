n, m, q = map(int, input().split())

score = [n]*m
clear = [[False]*m for _ in range(n)]
query = [input() for _ in range(q)]

for i in range(q):
    Q = query[i][0]
    if Q == '1':
        x, p = map(int, query[i].split())
        who = p-1
        ans = 0
        for j in range(m):
            if clear[who][j] == True:
                ans += score[j]
        print(ans)
    else:
        x, p, q = map(int, query[i].split())
        score[q-1] -= 1
        clear[p-1][q-1] = True

