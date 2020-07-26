n, x = map(int, input().split())
a = [int(x) for x in input().split()]
ans = 0
bx = str(bin(x))[2:]
i = 0
for j in reversed(bx):
    if j == '1':
        ans += a[i]
    i += 1
print(ans)
