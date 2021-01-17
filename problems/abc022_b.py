import collections
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
sp = collections.Counter(a)
for i in sp.values():
    if i >= 2:
        ans += i-1
print(ans)
    