import itertools
h, w, k = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(input()))

p = []
for i in range(1, 7):
    p.append(list(itertools.combinations(range(6), i)))

def cntblk(y, z):
    A = 0
    for a in range(h):
        if a in y:
            continue
        for b in range(w):
            if b in z:
                continue
            if c[a][b] == '#':
                A += 1
        if A > k:
            return 0
    return A

ans = []
for x in range(h):
    P = p[x]
    for y in range(w):
        Q = p[y]
        for z in P:
            for zz in Q:
                ans.append(cntblk(z, zz))

print(ans.count(k))