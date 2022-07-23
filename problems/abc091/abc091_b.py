import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

c = collections.Counter(s).most_common()
C = []
for i in range(len(c)):
    C.append([c[i][0], c[i][1]])

ans = []
for j in range(len(C)):
    if C[j][0] in t:
        C[j][1] -= t.count(C[j][0])
    ans.append(C[j][1])

print(max(ans) if max(ans) > 0 else 0)