n, m = map(int, input().split())
a = [0]*(n+1)
for j in range(m):
    pos = int(input())
    a[pos] = 1

MOD = 10**9+7

step = [0] * (n+1)
step[0] = 1
step[1] = 1

for i in range(n+1):
    if a[i] == 1:
        step[i] = 0
    else:
        if i != 0 and i != 1:
            step[i] = (step[i-1] + step[i-2]) % MOD

print(step[-1])
