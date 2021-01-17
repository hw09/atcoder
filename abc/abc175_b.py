import itertools

n = int(input())
l = [int(x) for x in input().split()]

ans = 0
for v in itertools.combinations(l, 3):
    if len(set(v)) == 3:
        a = v[0]
        b = v[1]
        c = v[2]
        if a+b > c and b+c > a and c+a >b:
            ans += 1
print(ans)