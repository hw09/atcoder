n = int(input())
a = [int(x) for x in input().split()]

x = a[0]
y = sum(a[1:])
ans = abs(x-y)

for i in range(1, n-1):
    x += a[i]
    y -= a[i]
    ans = min(ans, abs(x-y))
print(ans)