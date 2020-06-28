n, k = map(int, input().split())
p = [int(x) for x in input().split()]
p.sort()
ans = 0
for i in range(k):
    ans += p[i]
print(ans)
