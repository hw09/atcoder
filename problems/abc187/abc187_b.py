N = int(input())

p = []
for _ in range(N):
    p.append(list(map(int, input().split())))

ans = 0
slope = 1000
for i in range(N):
    for j in range(i+1, N):
        slope = (p[i][1] - p[j][1]) / (p[i][0] - p[j][0])
        if -1 <= slope <= 1:
            ans += 1
print(ans)
