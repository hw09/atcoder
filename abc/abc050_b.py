n = int(input())
t = [int(x) for x in input().split()]
m = int(input())
ans = 0
for i in range(m):
    p, x = map(int, input().split())
    for j in range(n):
        ans += t[j] if j != p-1 else x
    print(ans)
    ans = 0
        