n = int(input())
k = int(input())
x = [int(x) for x in input().split()]
ans = 0

for i in range(n):
    ans += x[i]*2 if x[i] < (k-x[i]) else (k-x[i])*2

print(ans)