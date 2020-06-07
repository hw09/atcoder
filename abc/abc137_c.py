n = int(input())
a = {}
ans = 0
for i in range(n):
    s = list(input())
    s.sort()
    S = ''.join(s)
    if S in a:
        a[S] += 1
    else:
        a[S] = 1

for j in a.values():
    ans += j * (j-1) // 2
print(ans)