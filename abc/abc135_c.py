n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    if b[i] <= a[i]:
        ans += b[i]
    elif b[i] > a[i] and b[i] <= a[i] + a[i+1]:
        ans += b[i]
        a[i+1] = a[i+1] - b[i] + a[i]
    else:
        ans += a[i] + a[i+1]
        a[i+1] = 0
print(ans)
