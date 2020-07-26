n = int(input())
INF = 10007

a = [0, 0, 1]

for i in range(2, n):
    a.append((a[i-2] + a[i-1] + a[i])%INF)

print(a[n-1])