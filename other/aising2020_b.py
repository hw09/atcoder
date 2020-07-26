n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(1, n+1):
    if i % 2 != 0 and a[i-1] % 2 != 0:
        ans += 1
print(ans)