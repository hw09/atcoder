import itertools
n = int(input())
l = [int(x) for x in range(1, 99)]
c = list(itertools.combinations_with_replacement(l, 3))

ans = [0]*(10**4)

for x, y, z in c:
    a = x**2 + y**2 + z**2 + x*y + y*z + z*x
    if a <= 10**4:
        s = {x, y, z}
        if len(s) == 1:
            ans[a-1] += 1
        elif len(s) == 2:
            ans[a-1] += 3
        elif len(s) == 3:
            ans[a-1] += 6
for i in range(n):
    print(ans[i])

