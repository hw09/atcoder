n = int(input())
a = [int(x) for x in input().split()]
suma = 0
cnt = 0
for i in range(n):
    if a[i] != 0:
        suma += a[i]
        cnt += 1
print(-(-suma//cnt))