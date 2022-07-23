import collections
w = list(input())
c = collections.Counter(w)
ans = 'Yes'
for s in c.values():
    if s % 2 != 0:
        ans = 'No'
print(ans)